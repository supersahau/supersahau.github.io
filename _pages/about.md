---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<!-- 页面容器 -->
<div class="page-container">
  <!-- 页面1: About Me + Educations -->
  <div id="page-1" class="page active">
    <div class='paper-box-text' markdown="1">
    <span class='anchor' id='about-me'></span>

    I am currently pursuing a Ph.D. degree in Intelligent Science and Technology at the School of Artificial Intelligence and Automation, Huazhong University of Science and Technology, supervised by Prof. Li Wei. <a href='https://scholar.google.com/citations?user=pj7fXtgAAAAJ&hl=en'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=Citations"></a>

    My research interest includes: 
    - *Broad Learning System*
    - *Deep Learning*
    - *Statistical Analysis and Prediction*
    - *Natural Language Processing*

    I helped my friends sort out the review material for the postgraduate entrance examination of "863 Probability & Mathematical Statistics" (*with few mistakes*). [[Download]](/pdf/概率论与数理统计.pdf) 


    <span class='anchor' id='-educations'></span>
    # 🎓 Educations
    - *2025.09 - present*, <a href="https://english.hust.edu.cn/"><img class="jpg" src="images/HUST.jpg" width="23pt"></a> [School of Artificial Intelligence and Automation, Huazhong University of Science and Technology](https://en-aia.hust.edu.cn/), Intelligent Science and Technology, Doctor, Ph.D.
    - *2022.09 - 2025.06*, <a href="http://english.qdu.edu.cn/"><img class="jpg" src="images/qdu.jpg" width="23pt"></a> [School of Automation, Qingdao University](http://zdh.qdu.edu.cn/), System Science, Master, M.Sc.
    - *2017.09 - 2021.06*, <a href="http://eng.ahau.edu.cn/"><img class="jpg" src="images/ahau.jpg" width="23pt"></a> [School of Engineering, Anhui Agriculture University](http://gxy.ahau.edu.cn/), Vehicle Engineering, Undergraduate, B.Eng.
    </div>
  </div>

  <!-- 页面2: News + Programs -->
  <div id="page-2" class="page">
    <div class='paper-box-text' markdown="1">
    <span class='anchor' id='-news'></span>
    # 🔥 News 
    - *2025.11*: 🔥🔥Our paper that titled "Sparse Bayesian Broad Learning System via Adaptive Lasso Priors for Robust Regression" was accepted to published in IEEE TRANSACTIONS ON NEURAL NETWORKS AND LEARNING SYSTEMS [[Link]](https://doi.org/10.1109/TNNLS.2025.3630247).
    - *2025.06*: 🔥🔥Mr. Chen was awarded the Outstanding Master's Thesis of Qingdao University for the year 2025 [[Certificate]](/images/qduyouxiuxueweilunwen.jpg).
    - *2024.10*: 🔥🔥Mr. Chen was awarded the National Scholarship for Postgraduates [[Certificate]](/images/guojiang.jpg).
 
    <span class='anchor' id='-programs'></span>
    # 📚 Programs
    - *2020.04 - 2021.04*, Student Development Support Program of the 5th "Excellent Talents Scheme" of Anhui Agricultural University, XSZZ202006, Sales Volume of New Energy Vehicles and Stock Market Fluctuations and Public Opinion Survey Analysis, Host, [[Notice]](http://xszz.ahau.edu.cn/info/1013/1793.htm) or [[List]](/Excel/安徽农业大学2020年第五期"优才计划"项目拟立项名单.xls)
    </div>
  </div>

  <!-- 页面3: Publications -->
  <div id="page-3" class="page">
    <div class='paper-box-text' markdown="1">
    <span class='anchor' id='-publications'></span>
    # 📝 Academic Publications 
    ### Graduate Theses
    ---
    - Be coming soon.

    *[注释]: -  **CHEN Tao**. Research on Sparse Bayesian Broad Learning System-Based Approaches for Regression Prediction[D]. Qingdao: *Qingdao University*, 2025.
    ### English Papers
    ---
    -  **Chen T**, Wang L J <sup><svg focusable="false" viewBox="0 0 102 128" height="20" title="Author email or social media contact details icon" class="icon icon-envelope react-xocs-author-icon u-fill-grey8"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg></sup>, C. L. Philip Chen. Sparse Bayesian broad learning system via adaptive lasso priors for robust regression[J]. *IEEE Transactions on Neural Networks and Learning Systems*, 2025, Early Access. [[HTML]](https://doi.org/10.1109/TNNLS.2025.3630247)

    -   **Chen T**, Wang L J <sup><svg focusable="false" viewBox="0 0 102 128" height="20" title="Author email or social media contact details icon" class="icon icon-envelope react-xocs-author-icon u-fill-grey8"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg></sup>, Liu Y, et al. Double-kernel based Bayesian approximation broad learning system with dropout[J]. *Neurocomputing*, 2024, 610: 128533.
    [[HTML]](https://doi.org/10.1016/j.neucom.2024.128533)

    -   **Chen T**, Wang L J <sup><svg focusable="false" viewBox="0 0 102 128" height="20" title="Author email or social media contact details icon" class="icon icon-envelope react-xocs-author-icon u-fill-grey8"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg></sup>, Liu Y, et al. DACBN: Dual attention convolutional broad network for fine-grained visual recognition[J]. *Pattern Recognition*, 2024, 156: 110749.
    [[HTML]](https://doi.org/10.1016/j.patcog.2024.110749)

    -  Wang Y J, Wang L J <sup><svg focusable="false" viewBox="0 0 102 128" height="20" title="Author email or social media contact details icon" class="icon icon-envelope react-xocs-author-icon u-fill-grey8"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg></sup>, **Chen T**. Broad learning system via adaptive maximum weighted correntropy[J]. *Neural Networks*, 2026, 193: 108032. [[HTML]](https://doi.org/10.1016/j.neunet.2025.108032)

    ### Chinese Papers
    --- 
    -   **CHEN Tao**, WANG Lijie <sup><svg focusable="false" viewBox="0 0 102 128" height="20" title="Author email or social media contact details icon" class="icon icon-envelope react-xocs-author-icon u-fill-grey8"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg></sup>, LIU Yang, et al. Bayesian approximate broad learning system with dropout structure[J]. *Control Theory & Applications*, 2025, 42(8): 1632-1640.
    [[HTML]](https://dx.doi.org/10.7641/CTA.2024.30087)

    **<svg focusable="false" viewBox="0 0 102 128" height="20" title="Author email or social media contact details icon" class="icon icon-envelope react-xocs-author-icon u-fill-grey8"><path d="M55.8 57.2c-1.78 1.31-5.14 1.31-6.9 0L17.58 34h69.54L55.8 57.19zM0 32.42l42.94 32.62c2.64 1.95 6.02 2.93 9.4 2.93s6.78-.98 9.42-2.93L102 34.34V24H0zM92 88.9L73.94 66.16l-8.04 5.95L83.28 94H18.74l18.38-23.12-8.04-5.96L10 88.94V51.36L0 42.9V104h102V44.82l-10 8.46V88.9"></path></svg>: Corresponding author.**
    </div>
  </div>

  <!-- 页面4: Honors + Conferences + Internships -->
  <div id="page-4" class="page">
    <div class='paper-box-text' markdown="1">
    <span class='anchor' id='-honors-and-awards'></span>
    # 📖 Honors and Awards
    - *Year 2025* Won **the Outstanding Master's Thesis** of Qingdao University [[Certificate]](/images/qduyouxiuxueweilunwen.jpg).
    - *Year 2024* Won **the National scholarship for Postgraduates** (Master) [[Certificate]](/images/guojiang.jpg),**the Outstanding Academic Innovation Achievement Award** of the 3rd Graduate Student Innovation Achievement Exhibition of Qingdao University in the Summer Semester of 2024.
    - *Year 2022* Won **the second prize** of Shandong Graduate "AI+" Innovation Competition.
    - *Year 2020* Won **the second prize** of the 18th SuperMap Cup GIS Competition, **the third prize** of the 10th National College Students' Market Survey and Analysis Competition and **the first prize** of Anhui Division, **the first prize** of Anhui Computer Game Competition for College Students, etc.
    - *Year 2019* Won **the third prize** of the 9th National College Students' Market Survey and Analysis Competition and **the first prize** of Anhui Division, **the third prize** of graduate group of Anhui College Studens' Statistical Modeling Contest, etc.

    <span class='anchor' id='-conferences'></span>
    # 🏭 Forums and Conferences
    - *2024.07*, The 3rd Graduate Student Innovation Achievement Exhibition of Qingdao University in the Summer Semester of 2024, Qingdao, Shandong.
    - *2024.05*, The 8th China Systems Science Congress, Wuhu, Anhui.
    - *2023.05*, The 2023 Postgraduate Academic Salon of Qingdao University "Realistic and Innovative, Research and Practice", Qingdao, Shandong. [[Notice]](https://mp.weixin.qq.com/s/iDcZ8NttA1ifqcynNizpSg)

    <span class='anchor' id='-internships'></span>
    # 💻 Internships
    - *2022.10 - 2023.06*, Engineering Journal of Wuhan University Editorial Department, **Internship Editor**.
    - *2021.05 - 2021.08*, Hefei Xiaolu Data Information Technology Co., Ltd., **Cloud Computing Engineer**.
    </div>
  </div>

  <!-- 页面5: Messages -->
  <div id="page-5" class="page">
    <div class='paper-box-text' markdown="1">
    <span class='anchor' id='-messages'></span>
    # 💬 Messages

    <script src="https://giscus.app/client.js"
            data-repo="supersahau/supersahau.github.io"
            data-repo-id="R_kgDOHjE2HA"
            data-category="Q&A"
            data-category-id="DIC_kwDOHjE2HM4CsW0m"
            data-mapping="pathname"
            data-strict="0"
            data-reactions-enabled="0"
            data-emit-metadata="0"
            data-input-position="top"
            data-theme="light"
            data-lang="en"
            crossorigin="anonymous"
            async>
    </script>
    </div>
  </div>
</div>

<!-- 简单的页面导航 -->
<div class="simple-page-nav">
  <button class="nav-btn prev-btn" onclick="switchPage(-1)">← 上一页</button>
  <span class="page-indicator">
    <span class="current-page">1</span> / <span class="total-pages">5</span>
  </span>
  <button class="nav-btn next-btn" onclick="switchPage(1)">下一页 →</button>
</div>

<style>
.page-container {
  position: relative;
  min-height: 60vh;
}

.page {
  display: none;
  animation: fadeIn 0.5s ease-in-out;
}

.page.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* 简单的页面导航样式 */
.simple-page-nav {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-top: 40px;
  padding: 20px;
  border-top: 1px solid #eaeaea;
}

.nav-btn {
  background: #2E86AB;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.nav-btn:hover {
  background: #1a5a7a;
}

.nav-btn:disabled {
  background: #cccccc;
  cursor: not-allowed;
}

.page-indicator {
  font-size: 16px;
  color: #666;
  font-weight: 500;
}

/* 保持原有paper-box-text样式不变 */
.paper-box-text {
  /* 您原有的所有样式都保持不变 */
}
</style>

<script>
// 页面状态
let currentPage = 1;
const totalPages = 5;

// 页面切换函数
function switchPage(direction) {
  const newPage = currentPage + direction;
  
  if (newPage >= 1 && newPage <= totalPages) {
    // 隐藏当前页面
    document.getElementById(`page-${currentPage}`).classList.remove('active');
    
    // 显示新页面
    document.getElementById(`page-${newPage}`).classList.add('active');
    
    // 更新当前页面
    currentPage = newPage;
    
    // 更新页面指示器
    document.querySelector('.current-page').textContent = currentPage;
    
    // 滚动到顶部
    window.scrollTo(0, 0);
    
    // 更新按钮状态
    updateNavButtons();
    
    // 更新URL
    updateURL();
  }
}

// 更新导航按钮状态
function updateNavButtons() {
  const prevBtn = document.querySelector('.prev-btn');
  const nextBtn = document.querySelector('.next-btn');
  
  prevBtn.disabled = currentPage === 1;
  nextBtn.disabled = currentPage === totalPages;
}

// 更新URL
function updateURL() {
  const pageMap = {
    1: 'about-me',
    2: 'news', 
    3: 'publications',
    4: 'honors-and-awards',
    5: 'messages'
  };
  
  const hash = pageMap[currentPage];
  history.replaceState(null, null, `/#${hash}`);
}

// 处理URL锚点导航
function handleHashNavigation() {
  const hash = window.location.hash.substring(1);
  const pageMap = {
    'about-me': 1,
    'educations': 1,
    'news': 2,
    'programs': 2,
    'publications': 3,
    'honors-and-awards': 4,
    'conferences': 4,
    'internships': 4,
    'messages': 5
  };
  
  if (hash && pageMap[hash]) {
    const targetPage = pageMap[hash];
    if (targetPage !== currentPage) {
      // 切换到目标页面
      document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
      document.getElementById(`page-${targetPage}`).classList.add('active');
      currentPage = targetPage;
      document.querySelector('.current-page').textContent = currentPage;
      updateNavButtons();
      window.scrollTo(0, 0);
    }
  }
}

// 键盘导航支持
document.addEventListener('keydown', function(event) {
  if (event.key === 'ArrowLeft') {
    switchPage(-1);
  } else if (event.key === 'ArrowRight') {
    switchPage(1);
  }
});

// 初始化
document.addEventListener('DOMContentLoaded', function() {
  // 初始处理URL
  handleHashNavigation();
  
  // 初始化按钮状态
  updateNavButtons();
  
  // 监听hash变化
  window.addEventListener('hashchange', handleHashNavigation);
});
</script>
