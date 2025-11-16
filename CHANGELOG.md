# 📝 CHANGELOG - Lịch Sử Thay Đổi

## Version 1.0.2 - 16/11/2025 (HOTFIX)

### 🔧 Fixed
- **Parser không đọc được file PASDV.docx trên Streamlit Cloud**
  - Sửa logic extract thông tin khách hàng (chỉ lấy người đầu tiên)
  - Sửa logic extract tổng nhu cầu vốn (lấy đúng 5 tỷ thay vì 1 VND)
  - Sửa tính toán tỷ lệ vốn đối ứng (20% thay vì 100 tỷ %)
  - Loại bỏ debug print statements
  - Thêm error handling tốt hơn

### 📁 Files Changed
- `src/docx_parser.py` - Parser chính (đã sửa)
- `src/docx_parser_v2.py` - Version 2 với error handling (NEW)
- `test_parser.py` - Script test parser (NEW)

### ✅ Test Results
```
Tên: Nguyễn Văn Minh ✅
CCCD: 001085012345 ✅
Tổng nhu cầu vốn: 5.000.000.000 VND ✅
Vốn đối ứng: 1.000.000.000 VND ✅
Tỷ lệ vốn đối ứng: 20% ✅
```

---

## Version 1.0.1 - 16/11/2025

### 🐛 Fixed
- Cải thiện requirements.txt (sử dụng >= thay vì ==)
- Thêm requirements-minimal.txt cho cài đặt nhanh
- Thêm INSTALLATION_TROUBLESHOOTING.md

### 📚 Documentation
- Thêm hướng dẫn xử lý lỗi cài đặt
- Thêm troubleshooting guide chi tiết

---

## Version 1.0.0 - 15/11/2025 (Initial Release)

### ✨ Features
- ✅ 8 Tab chức năng đầy đủ
- ✅ Upload và parse file DOCX
- ✅ Tính toán tài chính (DSR, LTV, dòng tiền)
- ✅ AI Gemini phân tích (2 modes)
- ✅ Chatbot AI
- ✅ Xuất Excel & PDF
- ✅ 5 loại biểu đồ
- ✅ Giao diện đẹp với Streamlit

### 📦 Project Structure
```
cadap_project/
├── app.py                  # Main application
├── requirements.txt        # Dependencies
├── src/                    # Source code
│   ├── config.py
│   ├── utils.py
│   └── docx_parser.py
├── logic/                  # Business logic
│   └── financial_calculator.py
├── ai/                     # AI integration
│   └── gemini_client.py
├── export/                 # Export modules
│   ├── excel_exporter.py
│   └── pdf_exporter.py
└── ui/                     # UI components
    └── chart_generator.py
```

### 📚 Documentation
- README.md - Hướng dẫn đầy đủ
- DEPLOY.md - Hướng dẫn deploy
- QUICKSTART.md - Hướng dẫn nhanh

---

## 🔄 Migration Guide

### Từ v1.0.1 → v1.0.2

**Chỉ cần update 1 file:**
```bash
# Option 1: Copy từ zip mới
cp cadap_project/src/docx_parser.py your_project/src/

# Option 2: Hoặc update toàn bộ
unzip cadap_project.zip
```

**Không cần thay đổi:**
- app.py (không đổi)
- Các module khác (không đổi)
- requirements.txt (không đổi)

**Sau khi update:**
1. Push lên GitHub
2. Reboot app trên Streamlit Cloud
3. Test với file PASDV.docx

---

## 🐞 Known Issues

### v1.0.2
- Không có issues đã biết

### v1.0.1
- Parser không đọc được file PASDV.docx → **FIXED in v1.0.2**

### v1.0.0
- Lỗi cài đặt với google-generativeai → **FIXED in v1.0.1**

---

## 📅 Roadmap

### v1.1.0 (Planned)
- [ ] Hỗ trợ nhiều format file hơn
- [ ] Tự động detect format và điều chỉnh parser
- [ ] Confidence score cho extracted fields
- [ ] Highlight low-confidence fields
- [ ] Multi-language support

### v1.2.0 (Future)
- [ ] Database integration
- [ ] User authentication
- [ ] Dashboard overview
- [ ] Batch processing
- [ ] Email notifications

---

## 🙏 Credits

- **Framework:** Streamlit
- **AI:** Google Gemini API
- **Charts:** Matplotlib
- **Documents:** python-docx, openpyxl, reportlab

---

## 📞 Support

- GitHub Issues: [Create Issue]
- Email: support@example.com
- Documentation: README.md

---

**Last Updated:** 16/11/2025
**Current Version:** 1.0.2
**Status:** ✅ Production Ready
