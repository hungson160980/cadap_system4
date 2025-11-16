#!/usr/bin/env python3
"""
Script test parser - Chạy để kiểm tra parser hoạt động
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.docx_parser import DocxParser
from src.utils import format_number

def test_parser(file_path):
    """Test parser với file"""
    print("=" * 80)
    print(f"Testing parser with: {file_path}")
    print("=" * 80)
    
    try:
        parser = DocxParser(file_path)
        data = parser.parse_full_document()
        
        print("\n✅ CUSTOMER INFO:")
        for key, value in data['customer_info'].items():
            print(f"  {key}: {value}")
        
        print("\n✅ LOAN INFO:")
        for key, value in data['loan_info'].items():
            if isinstance(value, (int, float)) and value > 1000:
                print(f"  {key}: {format_number(value)}")
            else:
                print(f"  {key}: {value}")
        
        print("\n✅ COLLATERAL INFO:")
        for key, value in data['collateral_info'].items():
            if isinstance(value, (int, float)) and value > 1000:
                print(f"  {key}: {format_number(value)}")
            else:
                print(f"  {key}: {value}")
        
        print("\n✅ FINANCIAL INFO:")
        for key, value in data['financial_info'].items():
            print(f"  {key}: {format_number(value)}")
        
        print("\n" + "=" * 80)
        print("✅ PARSER TEST PASSED!")
        print("=" * 80)
        
        return data
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Default test file
        file_path = "PASDV.docx"
    
    if os.path.exists(file_path):
        test_parser(file_path)
    else:
        print(f"❌ File not found: {file_path}")
        print("Usage: python test_parser.py <path_to_docx_file>")
