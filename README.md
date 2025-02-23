# 🌍 Web Scraper - External Link Extractor  

A simple yet effective **Web Scraper** that extracts external links from a webpage using **raw socket programming**.  

---

## 🚀 Features  
✅ Supports **HTTP & HTTPS**  
✅ Uses **Raw Sockets** for direct communication  
✅ Extracts **External Links** using **Regex**  
✅ **Minimal Dependencies** – Requires only Python!  
✅ **Structured Output** with clean formatting  

---

## 📥 Installation  

Clone this repository and navigate into the project directory:

```bash
git clone https://github.com/tanishqborse/Web-Scraper/link_scrapper.git
cd external-link-extractor
```
⚡ Usage
Run the script with a website URL as an argument:
```bash
python extract_links.py https://example.com
```

## 📌 Example Output

```bash
[+] Extracted Host: example.com

[+] External Links Found:
  - https://external1.com
  - https://external2.com

[+] Total External Links: 2
```
## 🛠 Requirements  

- 🐍 **Python 3**  
  No additional dependencies are required!  

## 🔥 How It Works  

1️⃣ **Establishes a raw socket connection** to the specified website.  
2️⃣ **Sends an HTTP GET request** to fetch the page content.  
3️⃣ **Parses the HTML response** and extracts all URLs.  
4️⃣ **Filters out internal links**, keeping only external ones.  

---

## 📜 License  

This project is licensed under the **MIT License**.  

---

## 🤝 Contributing  

🚀 **Have ideas to improve this project?** Feel free to contribute!  


✅ Fork the repository
✅ Create a new branch for your changes
✅ Submit a pull request

👨‍💻 Developed with ❤️ by Tanishq 
⭐ If you like this project, don’t forget to star it! ⭐
