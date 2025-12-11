# MaxProfitOptimizer
Dynamic web application to solve the Max Profit Problem using optimization algorithms. Input time units and get optimal property mix (Theatre, Pub, Commercial Park) for maximum earnings.

## 🎯 Live Demo

### ✨ [Open Interactive Web Application](https://akashbv6680.github.io/MaxProfitOptimizer)

**Try the Max Profit Optimizer now!** - No installation required, runs entirely in your browser.

## 📋 Features

✅ **Interactive Solver** - Input any time unit value and get instant results  
✅ **Automatic Test Verification** - Built-in verification for 3 test cases (n=7, 8, 13)  
✅ **Beautiful UI** - Modern gradient design with responsive layout  
✅ **No Dependencies** - Pure HTML/CSS/JavaScript - works everywhere  
✅ **Complete Solutions** - Shows all optimal combinations when multiple solutions exist  
✅ **100% Free** - Hosted on GitHub Pages with no costs  

## 🚀 Problem Statement

Mr. X owns a large strip of land on Mars and can build three types of properties:

| Property | Build Time | Earnings/Unit | Land Space |
|----------|------------|---------------|-----------|
| Theatre (T) | 5 units | $1500 | 2x1 |
| Pub (P) | 4 units | $1000 | 1x1 |
| Commercial Park (C) | 10 units | $2000 | 3x1 |

**Objective:** Find the optimal mix of properties to maximize earnings within n time units.

## 📊 Test Cases

✅ **Test Case 1:** n=7 → Expected Earnings: $3000  
✅ **Test Case 2:** n=8 → Expected Earnings: $4500  
✅ **Test Case 3:** n=13 → Expected Earnings: $16500  

## 💻 Technology Stack

- **HTML5** - Page structure
- **CSS3** - Styling and responsive design
- **JavaScript (ES6+)** - Dynamic calculations and interactivity
- **GitHub Pages** - Free hosting

## 📁 Files

- `index.html` - Complete web application (single file)
- `app.py` - Python Streamlit version (optional)
- `requirements.txt` - Python dependencies
- `README.md` - Documentation

## 🔧 How It Works

1. **Input Phase:** User enters the number of time units available
2. **Calculation Phase:** Algorithm explores all possible combinations
3. **Optimization:** Identifies the combination(s) with maximum earnings
4. **Display Phase:** Shows results with detailed breakdown

## 💡 Algorithm Complexity

- **Time Complexity:** O(n³) - Three nested loops through combinations
- **Space Complexity:** O(1) - Only stores the best solution(s)

## 🌐 Deployment (GitHub Pages - FREE)

This application is deployed for free using GitHub Pages:

1. Push HTML/CSS/JS files to GitHub repository
2. Enable GitHub Pages in Settings > Pages
3. Select "main" branch as source
4. Site is automatically deployed to: `https://username.github.io/repository-name`

**No servers, no costs, no hassle!**

## 📚 Learning Resources

- [GitHub Pages Documentation](https://pages.github.com/)
- [Optimization Algorithms](https://en.wikipedia.org/wiki/Optimization_(mathematics))
- [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)

## 👨‍💻 Author

**Akash BV**
- GitHub: [@akashBv6680](https://github.com/akashbv6680)
- Portfolio: Building AI/ML solutions
- Focus: Optimization algorithms & Web Applications
- 
## ⚡ Quick Start Guide

### For Web Users
1. **Visit the Application**: Open [this link](https://akashbv6680.github.io/MaxProfitOptimizer/)
2. **Enter Time Units**: Input the number of time units you want to optimize (1-1000)
3. **Click Calculate**: Press the "Calculate Max Profit" button
4. **View Results**: Instantly see the optimal property combination and earnings
5. **Check Test Cases**: Verify results against pre-defined test cases

### For Developers
```bash
# Clone the repository
git clone https://github.com/akashBv6680/MaxProfitOptimizer.git
cd MaxProfitOptimizer

# Open in browser (Web Version)
open index.html

# Or use with Python (Streamlit)
pip install -r requirements.txt
streamlit run app.py
```

### 🌐 Try on Streamlit Cloud

> **Streamlit Version Available:** If you prefer a Python-based interface, you can also run this application on Streamlit Cloud.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://maxprofitoptimizer-tt6sa93jzjor3myurmvyfh.streamlit.app/)
The Streamlit version provides the same powerful optimization engine with an interactive Python interface.

## 🎆 Use Cases & Applications

### Real-World Applications
- **Resource Allocation**: Optimizing property investments in limited time/budget
- **Portfolio Management**: Diversifying investments across multiple asset types
- **Production Planning**: Scheduling manufacturing of different products
- **Land Development**: Maximizing returns on Mars colonization projects
- **Educational Purpose**: Learning optimization algorithms and dynamic programming

### Interview Preparation
- Perfect for practicing optimization algorithm interviews
- Demonstrates problem-solving and algorithmic thinking
- Shows implementation skills in both JavaScript and Python
- Great portfolio project for Data Science/AI roles

## 📄 Contributing Guidelines

We welcome contributions! Here's how you can help:

### How to Contribute
1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/improvement`)
3. **Commit** your changes (`git commit -m 'Add improvement'`)
4. **Push** to the branch (`git push origin feature/improvement`)
5. **Open** a Pull Request

### Contribution Ideas
- Improve algorithm efficiency (reduce O(n³) complexity)
- Add more test cases
- Enhance UI/UX design
- Add visualization for profit distribution
- Implement additional optimization strategies
- Improve documentation
- Add multi-language support
- Create interactive tutorials

### Code Style
- Keep code clean and well-commented
- Use meaningful variable names
- Follow existing code structure
- Test thoroughly before submitting

## ❔ Frequently Asked Questions (FAQ)

### Q1: What does the solver do?
A: It finds the optimal combination of three property types (Theatre, Pub, Commercial Park) that maximize earnings within a given number of time units.

### Q2: Can I use this for other optimization problems?
A: Yes! The algorithm is adaptable. You can modify the property types, costs, and earnings to solve similar optimization problems.

### Q3: Why does it sometimes show multiple solutions?
A: When multiple combinations yield the same maximum profit, the solver displays all of them for completeness.

### Q4: What is the time complexity?
A: O(n³) - three nested loops are used to explore all possible combinations. For n≤1000, this runs instantly.

### Q5: Can I deploy this myself?
A: Absolutely! This project uses free GitHub Pages hosting. Just fork the repo and enable GitHub Pages in your settings.

### Q6: Why is the test case showing "FAILED"?
A: The test cases validate against the optimal solution. If your algorithm differs, it means there's a bug in the calculation logic. Check the algorithm implementation.

### Q7: How can I modify the properties?
Edit the `calculateMaxProfit()` function in `index.html` or `app.py` to change:
- Build times
- Earnings per unit
- Number of properties

### Q8: Is there a mobile version?
A: The current web version is responsive. Mobile support is planned for future releases.

### Q9: Can I use this for commercial projects?
A: Yes! The project is open source and available for both educational and commercial use.

### Q10: Who maintains this project?
A: [Akash BV](https://github.com/akashBv6680) created and maintains this project. Contributions are welcome!



## 📄 License

This project is open source and available for educational and commercial use.

---

**Built with ❤️ for Interview Assignments & Algorithm Learning**
