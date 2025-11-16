# src/docx_parser.py
"""Module trích xuất dữ liệu từ file DOCX - FIXED VERSION"""

import re
from typing import Dict, Any, Optional
from docx import Document


def parse_number(text: str) -> float:
    """Parse chuỗi số về float"""
    if not text or text == "":
        return 0.0
    try:
        cleaned = str(text).replace(".", "").replace(",", ".")
        return float(cleaned)
    except (ValueError, AttributeError):
        return 0.0


class DocxParser:
    """Class parse DOCX"""
    
    def __init__(self, file_path: str):
        """Khởi tạo parser"""
        self.doc = Document(file_path)
        self.paragraphs = [p.text.strip() for p in self.doc.paragraphs if p.text.strip()]
        self.text_content = "\n".join(self.paragraphs)
    
    def extract_customer_info(self) -> Dict[str, str]:
        """Trích xuất thông tin khách hàng"""
        name = ""
        cccd = ""
        address = ""
        phone = ""
        
        found_first = False
        
        for para in self.paragraphs:
            if not found_first and "1. Họ và tên:" in para:
                match = re.search(r'1\.\s*Họ và tên:\s*([^-\n]+)', para)
                if match:
                    name = match.group(1).strip()
                    found_first = True
            
            if found_first and not cccd and "CMND/CCCD" in para:
                match = re.search(r'(?:CMND/CCCD)[^:]*:\s*(\d{9,12})', para)
                if match:
                    cccd = match.group(1).strip()
            
            if found_first and not address and "Nơi cư trú:" in para:
                parts = para.split("Nơi cư trú:", 1)
                if len(parts) > 1:
                    address = parts[1].strip()
            
            if found_first and not phone and "Số điện thoại:" in para:
                match = re.search(r'Số điện thoại:\s*(\d{10,11})', para)
                if match:
                    phone = match.group(1).strip()
            
            if found_first and "2. Họ và tên:" in para:
                break
        
        return {
            'name': name if name else 'Khách hàng',
            'cccd': cccd,
            'address': address,
            'phone': phone
        }
    
    def extract_loan_info(self) -> Dict[str, Any]:
        """Trích xuất thông tin khoản vay"""
        total_need = 0.0
        equity = 0.0
        loan_amount = 0.0
        interest_rate = 8.5
        loan_term = 60
        purpose = "Kinh doanh"
        
        for para in self.paragraphs:
            if "1. Tổng nhu cầu vốn:" in para:
                match = re.search(r'Tổng nhu cầu vốn:\s*([\d.,]+)', para)
                if match:
                    total_need = parse_number(match.group(1))
            
            if "Vốn đối ứng tham gia" in para:
                match = re.search(r':\s*([\d.,]+)', para)
                if match:
                    equity = parse_number(match.group(1))
            
            if "Vốn vay Agribank số tiền:" in para:
                match = re.search(r'số tiền:\s*([\d.,]+)', para)
                if match:
                    loan_amount = parse_number(match.group(1))
            
            if "Mục đích vay:" in para:
                parts = para.split("Mục đích vay:", 1)
                if len(parts) > 1:
                    purpose = parts[1].strip()
            
            if "Thời hạn vay:" in para:
                match = re.search(r'Thời hạn vay:\s*(\d+)\s*tháng', para)
                if match:
                    loan_term = int(match.group(1))
            
            if "Lãi suất:" in para and "Thời hạn vay:" in para:
                match = re.search(r'Lãi suất:\s*(\d+[.,]?\d*)\s*%', para)
                if match:
                    interest_rate = float(match.group(1).replace(',', '.'))
        
        equity_ratio = (equity / total_need * 100) if total_need > 0 else 0
        
        return {
            'purpose': purpose,
            'total_need': total_need,
            'equity': equity,
            'loan_amount': loan_amount,
            'equity_ratio': equity_ratio,
            'interest_rate': interest_rate,
            'loan_term': loan_term,
            'payment_frequency': 'Tháng'
        }
    
    def extract_collateral_info(self) -> Dict[str, Any]:
        """Trích xuất thông tin tài sản bảo đảm"""
        asset_type = "Bất động sản"
        market_value = 0.0
        asset_address = ""
        ltv = 70.0
        legal_docs = ""
        
        in_collateral = False
        
        for para in self.paragraphs:
            if "5. Tài sản bảo đảm" in para:
                in_collateral = True
                continue
            
            if in_collateral:
                if "Tài sản 1:" in para:
                    match = re.search(r'Tài sản 1:\s*([^\.]+)', para)
                    if match:
                        asset_type = match.group(1).strip()
                    
                    if "Giá trị:" in para:
                        match = re.search(r'Giá trị:\s*([\d.,]+)', para)
                        if match:
                            market_value = parse_number(match.group(1))
                
                if in_collateral and "Địa chỉ:" in para:
                    parts = para.split("Địa chỉ:", 1)
                    if len(parts) > 1:
                        asset_address = parts[1].strip()
                
                if "LTV" in para or "Tỷ lệ cho vay" in para:
                    match = re.search(r'(\d+[.,]?\d*)\s*%', para)
                    if match:
                        ltv = float(match.group(1).replace(',', '.'))
                
                if "Giấy chứng nhận" in para:
                    legal_docs = para
                
                if "III." in para:
                    break
        
        return {
            'asset_type': asset_type,
            'market_value': market_value,
            'asset_address': asset_address,
            'ltv': ltv,
            'legal_docs': legal_docs if legal_docs else 'Sổ đỏ'
        }
    
    def extract_financial_info(self) -> Dict[str, float]:
        """Trích xuất thông tin tài chính"""
        monthly_income = 0.0
        monthly_expense = 0.0
        other_debt = 0.0
        
        for para in self.paragraphs:
            if "Tổng thu nhập" in para and "tháng" in para.lower():
                match = re.search(r':\s*([\d.,]+)', para)
                if match:
                    monthly_income = parse_number(match.group(1))
            
            if "Tổng chi phí hàng tháng:" in para:
                match = re.search(r':\s*([\d.,]+)', para)
                if match:
                    monthly_expense = parse_number(match.group(1))
        
        return {
            'monthly_income': monthly_income,
            'monthly_expense': monthly_expense,
            'other_debt': other_debt
        }
    
    def parse_full_document(self) -> Dict[str, Any]:
        """Parse toàn bộ document"""
        return {
            'customer_info': self.extract_customer_info(),
            'loan_info': self.extract_loan_info(),
            'collateral_info': self.extract_collateral_info(),
            'financial_info': self.extract_financial_info(),
            'raw_text': self.text_content
        }
