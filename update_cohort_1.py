import re

file_path = "/Users/nikhilgour/Documents/Aescode Co./stitch_aescode_accelerator_site/cohort_1_2026_update/cohort1.html"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update <style>
style_target = """<style>
        .dot-grid {
            background-image: radial-gradient(circle, #021934 1px, transparent 1px);
            background-size: 24px 24px;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
    </style>"""
    
style_replace = """<style>
        .dot-grid {
            background-image: radial-gradient(circle, #021934 1px, transparent 1px);
            background-size: 24px 24px;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        @keyframes marquee-left {
            from { transform: translateX(0); }
            to { transform: translateX(-50%); }
        }
        @keyframes marquee-right {
            from { transform: translateX(-50%); }
            to { transform: translateX(0); }
        }
        .marquee-track {
            display: flex;
            width: max-content;
        }
        .row-1 {
            animation: marquee-left 40s linear infinite;
        }
        .row-2 {
            animation: marquee-right 40s linear infinite;
            margin-top: 16px;
        }
        .marquee-container:hover .row-1, .marquee-container:hover .row-2 {
            animation-play-state: paused;
        }
    </style>"""
text = text.replace(style_target, style_replace)

# 2. Update Nav
nav_target = """<div class="hidden md:flex items-center space-x-8">
<a class="text-slate-500 dark:text-slate-400 font-medium hover:text-[#021934] dark:hover:text-white transition-colors duration-300 Public Sans text-xs tracking-widest uppercase" href="#" style="">Home</a>
<a class="text-slate-500 dark:text-slate-400 font-medium hover:text-[#021934] dark:hover:text-white transition-colors duration-300 Public Sans text-xs tracking-widest uppercase" href="#" style="">About</a>
<a class="text-[#021934] dark:text-white border-b border-[#021934] dark:border-white pb-1 Public Sans text-xs tracking-widest uppercase" href="#" style="">Cohort 1</a>
<a class="text-slate-500 dark:text-slate-400 font-medium hover:text-[#021934] dark:hover:text-white transition-colors duration-300 Public Sans text-xs tracking-widest uppercase" href="#" style="">Problems</a>
<a class="text-slate-500 dark:text-slate-400 font-medium hover:text-[#021934] dark:hover:text-white transition-colors duration-300 Public Sans text-xs tracking-widest uppercase" href="#" style="">Contact</a>
</div>"""

nav_replace = """<div class="hidden md:flex items-center space-x-8">
<a class="font-label text-[10px] uppercase tracking-[0.2em] text-[#707785] hover:text-[#021934] transition-colors duration-300" href="#">HOME</a>
<a class="font-label text-[10px] uppercase tracking-[0.2em] text-[#707785] hover:text-[#021934] transition-colors duration-300" href="#">ABOUT</a>
<a class="font-label text-[10px] uppercase tracking-[0.2em] text-[#021934] border-b-[1px] border-[#021934] pb-1" href="#">COHORT 1</a>
<a class="font-label text-[10px] uppercase tracking-[0.2em] text-[#707785] hover:text-[#021934] transition-colors duration-300" href="#">AI ETHICS</a>
<a class="font-label text-[10px] uppercase tracking-[0.2em] text-[#707785] hover:text-[#021934] transition-colors duration-300" href="#">CONTACT</a>
</div>"""
text = text.replace(nav_target, nav_replace)

# 3. Replace MENTORS & JUDGES section with all new sections
# First, find the MENTORS & JUDGES section string accurately since it might have whitespaces
mentors_judgesPattern = re.compile(r'<section class="mb-48">\s*<div class="grid grid-cols-12 gap-8">\s*<div class="col-span-12 lg:col-span-4 mb-12 lg:mb-0">\s*<h2 class="font-label text-\[10px\] tracking-\[0.2em\] uppercase text-primary"[^>]*>MENTORS &amp; JUDGES.*?</div>\s*</div>\s*</section>', re.DOTALL)

new_sections_html = """
<!-- 05. Problem Statements -->
<section class="mb-48">
  <div class="grid grid-cols-12 gap-8 items-start">
    <div class="col-span-12 lg:col-span-4 mb-12 lg:mb-0">
      <h2 class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] sticky top-32">PROBLEMS</h2>
    </div>
    <div class="col-span-12 lg:col-span-8">
      <div id="accordion-container" class="flex flex-col">
        <!-- Card 1 -->
        <button class="problem-card group text-left w-full bg-[#FFFFFF] rounded-[2px] border-t-[0.5px] border-[#C4C6CE] py-6 hover:bg-[#FCF9F8] transition-colors" data-index="0">
          <div class="flex justify-between items-center mb-2">
            <span class="font-label text-[10px] uppercase text-[#707785]">DIABETIC CARE</span>
            <span class="material-symbols-outlined text-[#707785] transition-transform duration-200 plus-icon">add</span>
          </div>
          <h3 class="font-headline text-[24px] text-[#021934] font-normal mb-0">AI-Based Prediction of High-Risk Plantar Pressure Zones</h3>
          
          <div class="accordion-content hidden mt-4">
            <p class="font-body text-[13px] text-[#707785] leading-[1.6] mb-6">
              Identifying high-pressure areas in diabetic patients to prevent ulceration through early biomechanical intervention.
            </p>
            <div class="grid grid-cols-2 gap-4 text-left">
              <div>
                <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">ML TASK</span>
                <span class="font-body text-[12px] text-[#1C1B1B]">Supervised ML — Classification / Risk Prediction</span>
              </div>
              <div>
                <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">EXPECTED OUTPUT</span>
                <span class="font-body text-[12px] text-[#1C1B1B]">Pressure hotspot detection map · Ulcer risk score for foot regions</span>
              </div>
            </div>
          </div>
        </button>
        <!-- Card 2 -->
        <button class="problem-card group text-left w-full bg-[#FFFFFF] rounded-[2px] border-t-[0.5px] border-[#C4C6CE] py-6 hover:bg-[#FCF9F8] transition-colors" data-index="1">
          <div class="flex justify-between items-center mb-2">
            <span class="font-label text-[10px] uppercase text-[#707785]">PATIENT MONITORING</span>
            <span class="material-symbols-outlined text-[#707785] transition-transform duration-200 plus-icon">add</span>
          </div>
          <h3 class="font-headline text-[24px] text-[#021934] font-normal mb-0">AI-Based Early Warning System for Patient Physiological Deterioration</h3>
          
          <div class="accordion-content hidden mt-4">
            <p class="font-body text-[13px] text-[#707785] leading-[1.6] mb-6">
              Detecting subtle patterns in vital signs that precede clinical decompensation in acute care settings.
            </p>
            <div class="grid grid-cols-2 gap-4 text-left">
              <div>
                <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">ML TASK</span>
                <span class="font-body text-[12px] text-[#1C1B1B]">Time-Series Prediction / Binary Classification</span>
              </div>
              <div>
                <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">EXPECTED OUTPUT</span>
                <span class="font-body text-[12px] text-[#1C1B1B]">Real-time risk score with clinical reasoning flags</span>
              </div>
            </div>
          </div>
        </button>
        <!-- Card 3 -->
        <button class="problem-card group text-left w-full bg-[#FFFFFF] rounded-[2px] border-t-[0.5px] border-[#C4C6CE] py-6 hover:bg-[#FCF9F8] transition-colors" data-index="2">
          <div class="flex justify-between items-center mb-2">
            <span class="font-label text-[10px] uppercase text-[#707785]">BONE HEALTH</span>
            <span class="material-symbols-outlined text-[#707785] transition-transform duration-200 plus-icon">add</span>
          </div>
          <h3 class="font-headline text-[24px] text-[#021934] font-normal mb-0">AI-Based Osteoporosis Risk Screening from Routine X-Ray Radiographs</h3>
          
          <div class="accordion-content hidden mt-4">
            <p class="font-body text-[13px] text-[#707785] leading-[1.6] mb-6">
              Analyzing opportunistic imaging data to screen for low bone density in asymptomatic populations.
            </p>
            <div class="grid grid-cols-2 gap-4 text-left">
              <div>
                <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">ML TASK</span>
                <span class="font-body text-[12px] text-[#1C1B1B]">Computer Vision — Image Classification</span>
              </div>
              <div>
                <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">EXPECTED OUTPUT</span>
                <span class="font-body text-[12px] text-[#1C1B1B]">Probabilistic fracture risk index · Binary or multi-class classification</span>
              </div>
            </div>
          </div>
        </button>
        <!-- Card 4 -->
        <button class="problem-card group text-left w-full bg-[#FFFFFF] rounded-[2px] border-t-[0.5px] border-[#C4C6CE] py-6 hover:bg-[#FCF9F8] transition-colors" data-index="3">
          <div class="flex justify-between items-center mb-2">
            <span class="font-label text-[10px] uppercase text-[#707785]">REHABILITATION</span>
            <span class="material-symbols-outlined text-[#707785] transition-transform duration-200 plus-icon">add</span>
          </div>
          <h3 class="font-headline text-[24px] text-[#021934] font-normal mb-0">AI-Based Detection of Incorrect Exercise Form Using Human Pose Estimation</h3>
          
          <div class="accordion-content hidden mt-4">
            <p class="font-body text-[13px] text-[#707785] leading-[1.6] mb-6">
              Providing real-time feedback on kinetic alignment to ensure safe and effective home-based physical therapy.
            </p>
            <div class="grid grid-cols-2 gap-4 text-left">
              <div>
                <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">ML TASK</span>
                <span class="font-body text-[12px] text-[#1C1B1B]">Computer Vision + Classification / Pose Estimation</span>
              </div>
              <div>
                <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">EXPECTED OUTPUT</span>
                <span class="font-body text-[12px] text-[#1C1B1B]">Correction vectors and form quality score</span>
              </div>
            </div>
          </div>
        </button>
        <!-- Card 5 -->
        <button class="problem-card group text-left w-full bg-[#FFFFFF] rounded-[2px] border-t-[0.5px] border-[#C4C6CE] py-6 hover:bg-[#FCF9F8] transition-colors" data-index="4">
          <div class="flex justify-between items-center mb-2">
            <span class="font-label text-[10px] uppercase text-[#707785]">STROKE</span>
            <span class="material-symbols-outlined text-[#707785] transition-transform duration-200 plus-icon">add</span>
          </div>
          <h3 class="font-headline text-[24px] text-[#021934] font-normal mb-0">AI-Based Infarct Volume Estimation from Non-Contrast CT</h3>
          
          <div class="accordion-content hidden mt-4">
            <p class="font-body text-[13px] text-[#707785] leading-[1.6] mb-6">
              Automating the precise measurement of ischemic core and penumbra to guide urgent thrombectomy decisions.
            </p>
            <div class="grid grid-cols-2 gap-4 text-left">
              <div>
                <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">ML TASK</span>
                <span class="font-body text-[12px] text-[#1C1B1B]">Medical Image Segmentation + Regression</span>
              </div>
              <div>
                <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">EXPECTED OUTPUT</span>
                <span class="font-body text-[12px] text-[#1C1B1B]">Quantified volume in mL and vascular territory map · Segmentation overlay on CT slices</span>
              </div>
            </div>
          </div>
        </button>
      </div>
    </div>
  </div>
</section>

<!-- 06. Judges -->
<section class="mb-48">
  <div class="grid grid-cols-12 gap-8 items-start">
    <div class="col-span-12 lg:col-span-4 mb-12 lg:mb-0">
      <h2 class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] sticky top-32">EVALUATION COMMITTEE</h2>
    </div>
    <div class="col-span-12 lg:col-span-8">
      <h3 class="font-headline italic text-[48px] text-[#021934] mb-[80px]">The Cohort Judges.</h3>
      
      <!-- Judge 01 -->
      <div class="grid grid-cols-12 gap-[80px] mb-[80px] items-center">
        <div class="col-span-5">
          <img src="../../Images/Judges/dhane.png" alt="Dr. Dheeraj Dhane" class="w-full aspect-[4/5] object-cover rounded-[2px] grayscale">
        </div>
        <div class="col-span-7">
          <span class="font-label text-[9px] uppercase text-[#C4C6CE] mb-4 block">01 / SENIOR EVALUATOR</span>
          <h4 class="font-headline italic text-[28px] text-[#021934] mb-1">Dr. Dheeraj Dhane</h4>
          <span class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] block mb-6">SENIOR MEMBER, IEEE</span>
          <p class="font-headline italic text-[20px] text-[#1C1B1B] max-w-[480px] mb-6">
            "A distinguished scholar in signal processing and computational systems, Dr. Dhane brings rigorous academic standards to the technical evaluation process."
          </p>
          <p class="font-body text-[13px] text-[#707785] leading-[1.75] mb-6">
            Dr. Dhane holds a Ph.D. from the prestigious IIT Kharagpur, and has over 15 years of teaching experience. He is a Senior Member of IEEE, a distinction held by only a select few, and serves as a Distinguished Reviewer for some of the most reputed journals in the field, including Pattern Recognition Letters, IEEE Transactions on Industrial Informatics, Multimedia Tools and Applications, Computers in Biology and Medicine, and IEEE Access.
          </p>
          <div class="flex flex-wrap gap-8">
            <div>
              <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">FOCUS</span>
              <span class="font-body text-[11px] text-[#1C1B1B]">Signal Processing &amp; Systems</span>
            </div>
            <div>
              <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">AFFILIATION</span>
              <span class="font-body text-[11px] text-[#1C1B1B]">IEEE Senior Member</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Judge 02 -->
      <div class="grid grid-cols-12 gap-[80px] mb-[80px] items-center">
        <div class="col-span-7">
          <span class="font-label text-[9px] uppercase text-[#C4C6CE] mb-4 block">02 / TECHNICAL LEAD</span>
          <h4 class="font-headline italic text-[28px] text-[#021934] mb-1">Mr. Bhavik Kanekar</h4>
          <span class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] block mb-6">SYSTEMS SPECIALIST, KCDH</span>
          <p class="font-headline italic text-[20px] text-[#1C1B1B] max-w-[480px] mb-6">
            "Expert in large-scale data systems and clinical data hygiene, Bhavik Kanekar focuses on the scalability and structural integrity of healthcare informatics."
          </p>
          <p class="font-body text-[13px] text-[#707785] leading-[1.75] mb-6">
            Bhavik Kanekar holds a B.E. and MTech from Mumbai University and is currently pursuing a PhD at the Koita Centre for Digital Health (KCDH), IIT Bombay. His work focuses on the application of computer vision and AI/ML in the healthcare domain, with a particular emphasis on accelerating diagnostics and treatment planning.
          </p>
          <div class="flex flex-wrap gap-8">
            <div>
              <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">FOCUS</span>
              <span class="font-body text-[11px] text-[#1C1B1B]">Data Engineering</span>
            </div>
            <div>
              <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">AFFILIATION</span>
              <span class="font-body text-[11px] text-[#1C1B1B]">KCDH Research Lab</span>
            </div>
          </div>
        </div>
        <div class="col-span-5">
          <img src="../../Images/Judges/kanekar.png" alt="Mr. Bhavik Kanekar" class="w-full aspect-[4/5] object-cover rounded-[2px] grayscale">
        </div>
      </div>

      <!-- Judge 03 -->
      <div class="grid grid-cols-12 gap-[80px] mb-[80px] items-center">
        <div class="col-span-5">
          <img src="../../Images/Judges/goswami.png" alt="Mr. Buddhadev Goswami" class="w-full aspect-[4/5] object-cover rounded-[2px] grayscale">
        </div>
        <div class="col-span-7">
          <span class="font-label text-[9px] uppercase text-[#C4C6CE] mb-4 block">03 / IMPLEMENTATION LEAD</span>
          <h4 class="font-headline italic text-[28px] text-[#021934] mb-1">Mr. Buddhadev Goswami</h4>
          <span class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] block mb-6">SENIOR ENGINEER, KCDH</span>
          <p class="font-headline italic text-[20px] text-[#1C1B1B] max-w-[480px] mb-6">
            "Focusing on the intersection of healthcare technology and rapid prototyping, Buddhadev Goswami ensures that digital solutions are both innovative and deployable."
          </p>
          <p class="font-body text-[13px] text-[#707785] leading-[1.75] mb-6">
            Buddhadev Goswami is a 4th-year Ph.D. scholar at the Koita Centre for Digital Health (KCDH), IIT Bombay. His research lies in the field of computer vision, with a strong emphasis on RGB image-based analysis for healthcare and medical imaging applications. His technical expertise and domain-focused research make him exceptionally well-equipped to guide teams working on imaging-driven diagnostic challenges.
          </p>
          <div class="flex flex-wrap gap-8">
            <div>
              <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">FOCUS</span>
              <span class="font-body text-[11px] text-[#1C1B1B]">Healthcare Deployment</span>
            </div>
            <div>
              <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">AFFILIATION</span>
              <span class="font-body text-[11px] text-[#1C1B1B]">KCDH Engineering</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Judge 04 -->
      <div class="grid grid-cols-12 gap-[80px] mb-[80px] items-center">
        <div class="col-span-7">
          <span class="font-label text-[9px] uppercase text-[#C4C6CE] mb-4 block">04 / CLINICAL PRINCIPAL</span>
          <h4 class="font-headline italic text-[28px] text-[#021934] mb-1">Dr. Dulari Gupta</h4>
          <span class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] block mb-6">NEUROLOGIST</span>
          <p class="font-headline italic text-[20px] text-[#1C1B1B] max-w-[480px] mb-6">
            "As a leading neurologist, Dr. Gupta provides critical insight into the cognitive impact and neuro-ethical dimensions of human-computer interaction."
          </p>
          <p class="font-body text-[13px] text-[#707785] leading-[1.75] mb-6">
            Dr. Dulari Gupta is a well-known Neurologist associated with Deenanath Mangeshkar Hospital and Research Centre. She has 17 years of experience in Neurology and has worked as an expert in different cities in India. Dr. Dulari Gupta has contributed to handling numerous complex medical cases in several hospitals. She is known for her attention to accurate diagnosis and treating patients empathetically. The specialty interests of Dr. Dulari Gupta are Stroke Thrombolysis, Parkinson's Disease, Epilepsy Surgeries and Neurocritical Care.
          </p>
          <div class="flex flex-wrap gap-8">
            <div>
              <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">FOCUS</span>
              <span class="font-body text-[11px] text-[#1C1B1B]">Neuro-UX &amp; Cognitive Ethics</span>
            </div>
            <div>
              <span class="font-label text-[9px] uppercase tracking-[0.15em] text-[#C4C6CE] block mb-1">AFFILIATION</span>
              <span class="font-body text-[11px] text-[#1C1B1B]">Medical Board</span>
            </div>
          </div>
        </div>
        <div class="col-span-5">
          <img src="../../Images/Judges/gupta.png" alt="Dr. Dulari Gupta" class="w-full aspect-[4/5] object-cover rounded-[2px] grayscale">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 07. Mentors -->
<section class="mb-48">
  <div class="grid grid-cols-12 gap-8 items-start">
    <div class="col-span-12 lg:col-span-4 mb-12 lg:mb-0">
      <h2 class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] sticky top-32">RESEARCH MENTORS</h2>
    </div>
    <div class="col-span-12 lg:col-span-8">
      <h3 class="font-headline italic text-[40px] text-[#021934] mb-12">The Mentors.</h3>
      
      <!-- Mentor 01 -->
      <div class="flex gap-8 border-t-[0.5px] border-[#C4C6CE] py-[32px]">
        <div class="shrink-0 w-[80px] h-[100px]">
          <img src="../../Images/mentors/gaur.png" alt="Mr. Viraj Gaur" class="w-full h-full object-cover rounded-[2px] grayscale">
        </div>
        <div class="flex-1 flex flex-col justify-between">
          <div>
            <span class="font-label text-[9px] uppercase text-[#C4C6CE] mb-2 block">01 / KCDH MENTOR</span>
            <div class="flex justify-between items-baseline mb-1">
              <h4 class="font-headline text-[22px] text-[#021934] font-normal">Mr. Viraj Gaur</h4>
              <span class="font-label text-[10px] uppercase tracking-[0.15em] text-[#C4C6CE]">IMAGE PROCESSING</span>
            </div>
            <span class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] block mb-4">MACHINE LEARNING</span>
            <p class="font-body text-[13px] text-[#707785] leading-[1.6] max-w-[560px]">
              Mr. Viraj Gaur holds a Bachelor's and Master's degree in Computer Science from Queen's University Belfast (2022), followed by an Engineering Doctorate in Software Technology from Eindhoven University of Technology. His academic and professional background spans software development, automation, and published research in cyber-physical systems and image processing. He currently works at the intersection of neurology and technology, with a specialisation in image processing and deep learning, making him exceptionally well-placed to mentor teams working in the medtech space.
            </p>
          </div>
        </div>
      </div>

      <!-- Mentor 02 -->
      <div class="flex gap-8 border-t-[0.5px] border-[#C4C6CE] py-[32px]">
        <div class="shrink-0 w-[80px] h-[100px]">
          <img src="../../Images/mentors/ghosh.png" alt="Dr. Subham Ghosh" class="w-full h-full object-cover rounded-[2px] grayscale">
        </div>
        <div class="flex-1 flex flex-col justify-between">
          <div>
            <span class="font-label text-[9px] uppercase text-[#C4C6CE] mb-2 block">02 / KCDH MENTOR</span>
            <div class="flex justify-between items-baseline mb-1">
              <h4 class="font-headline text-[22px] text-[#021934] font-normal">Dr. Subham Ghosh</h4>
              <span class="font-label text-[10px] uppercase tracking-[0.15em] text-[#C4C6CE]">WEARABLE SYSTEMS</span>
            </div>
            <span class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] block mb-4">POSTDOCTORAL FELLOW, KCDH IIT BOMBAY</span>
            <p class="font-body text-[13px] text-[#707785] leading-[1.6] max-w-[560px]">
              Dr. Subham Ghosh is a Postdoctoral Fellow at the Koita Centre for Digital Health (KCDH), IIT Bombay. His work brings together wearable electronics, advanced signal processing, and shallow deep-learning models optimized for edge computing. His interdisciplinary expertise positions him strongly to guide teams working on real-time healthcare monitoring and intelligent sensing systems.
            </p>
          </div>
        </div>
      </div>

      <!-- Mentor 03 -->
      <div class="flex gap-8 border-t-[0.5px] border-[#C4C6CE] py-[32px]">
        <div class="shrink-0 w-[80px] h-[100px]">
          <img src="../../Images/mentors/banerjee.png" alt="Mr. Shayantan Banerjee" class="w-full h-full object-cover rounded-[2px] grayscale">
        </div>
        <div class="flex-1 flex flex-col justify-between">
          <div>
            <span class="font-label text-[9px] uppercase text-[#C4C6CE] mb-2 block">03 / KCDH MENTOR</span>
            <div class="flex justify-between items-baseline mb-1">
              <h4 class="font-headline text-[22px] text-[#021934] font-normal">Mr. Shayantan Banerjee</h4>
              <span class="font-label text-[10px] uppercase tracking-[0.15em] text-[#C4C6CE]">TRANSLATIONAL RESEARCH</span>
            </div>
            <span class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] block mb-4">PHD SCHOLAR, KCDH IIT BOMBAY</span>
            <p class="font-body text-[13px] text-[#707785] leading-[1.6] max-w-[560px]">
              Mr. Shayantan Banerjee is a PhD student at the Koita Centre for Digital Health (KCDH), IIT Bombay, working in computational omics. His research focuses on developing machine learning models using clinical data, with a strong emphasis on interpretability and generalizability. His expertise sits at the intersection of healthcare, data science, and translational research, making him exceptionally well-suited to mentor teams working on medtech challenges.
            </p>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- 08. Testimonials -->
<section class="mb-48">
  <div class="grid grid-cols-12 gap-8 items-start">
    <div class="col-span-12 lg:col-span-4 mb-12 lg:mb-0">
      <h2 class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] sticky top-32">FROM THE COHORT</h2>
    </div>
    <div class="col-span-12 lg:col-span-8">
      <h3 class="font-headline italic text-[40px] text-[#021934] mb-4">What They Built. What They Said.</h3>
      <p class="font-body text-[14px] text-[#707785] italic mb-12">
        "Testimonials, winner stories, and documentation from Cohort 1 participants will appear here."
      </p>
      
      <div class="bg-[#FFFFFF] border-[0.5px] border-[#C4C6CE] rounded-[2px] p-12 h-[240px] flex flex-col justify-center items-center text-center">
        <span class="font-headline text-[80px] text-[#C4C6CE] leading-none mb-4">"</span>
        <span class="font-label text-[9px] uppercase tracking-[0.2em] text-[#C4C6CE]">WINNER TESTIMONIAL — COMING SOON</span>
      </div>
    </div>
  </div>
</section>

<!-- 09. Archive Marquee -->
<section class="mb-48">
  <div class="grid grid-cols-12 gap-8 items-start mb-12">
    <div class="col-span-12 lg:col-span-4 mb-12 lg:mb-0">
      <h2 class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] sticky top-32">COHORT 1 ARCHIVE</h2>
    </div>
    <div class="col-span-12 lg:col-span-8">
      <h3 class="font-headline italic text-[40px] text-[#021934]">The Event. Documented.</h3>
    </div>
  </div>

  <div class="marquee-container overflow-hidden w-full -mx-8 px-8 py-[48px] relative group">
    <!-- Row 1 -->
    <div class="marquee-track row-1 flex w-max gap-[16px]">
"""

for i in range(8):
    new_sections_html += f"""
      <div class="w-[280px] h-[200px] shrink-0 bg-[#E5E2E1] rounded-[8px] flex items-center justify-center">
        <span class="font-label text-[9px] uppercase tracking-[0.2em] text-[#707785]">EVENT PHOTO</span>
      </div>
      <div class="w-[280px] h-[200px] shrink-0 bg-[#021934] rounded-[8px] flex flex-col items-center justify-center text-center px-4">
        <span class="font-label text-[9px] uppercase text-[rgba(255,255,255,0.4)] mb-2">COHORT 1 WINNER</span>
        <h4 class="font-headline italic text-[22px] text-[#FFFFFF] mb-2">Category Award</h4>
        <span class="font-body text-[11px] text-[rgba(255,255,255,0.6)]">₹10,000 — Innovation Grant</span>
      </div>
"""

new_sections_html += """
    </div>

    <!-- Row 2 -->
    <div class="marquee-track row-2 flex w-max gap-[16px]">
"""

for i in range(8):
    new_sections_html += f"""
      <div class="w-[280px] h-[200px] shrink-0 bg-[#021934] rounded-[8px] flex flex-col items-center justify-center text-center px-4">
        <span class="font-label text-[9px] uppercase text-[rgba(255,255,255,0.4)] mb-2">COHORT 1 WINNER</span>
        <h4 class="font-headline italic text-[22px] text-[#FFFFFF] mb-2">Category Award</h4>
        <span class="font-body text-[11px] text-[rgba(255,255,255,0.6)]">₹10,000 — Innovation Grant</span>
      </div>
      <div class="w-[280px] h-[200px] shrink-0 bg-[#E5E2E1] rounded-[8px] flex items-center justify-center">
        <span class="font-label text-[9px] uppercase tracking-[0.2em] text-[#707785]">EVENT PHOTO</span>
      </div>
"""

new_sections_html += """
    </div>
  </div>
</section>
"""

text = re.sub(mentors_judgesPattern, new_sections_html, text)

# 4. Insert Modal Overlay right before </body>
modal_html = """
<!-- Modal Overlay -->
<div id="problem-modal" class="fixed inset-0 z-50 flex items-center justify-center opacity-0 pointer-events-none transition-opacity duration-200" style="background-color: rgba(2, 25, 52, 0.6); backdrop-filter: blur(8px);">
  <div id="problem-modal-content" class="bg-[#FFFFFF] rounded-[12px] p-12 max-w-[680px] w-full max-h-[90vh] overflow-y-auto relative transform translate-y-[24px] scale-[0.97] transition-transform opacity-0 duration-280" style="box-shadow: 0 24px 64px rgba(2, 25, 52, 0.18); transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);">
    <button id="modal-close" class="absolute top-8 right-8 font-label text-[18px] text-[#707785] hover:text-[#021934] transition-colors">×</button>
    
    <span id="modal-category" class="font-label text-[10px] uppercase tracking-[0.2em] text-[#707785] block mb-2">CATEGORY</span>
    <h2 id="modal-title" class="font-headline text-[32px] text-[#021934] font-normal mb-8">Title</h2>
    
    <div class="border-t-[0.5px] border-[#C4C6CE] pt-6 mb-6 text-left">
      <span class="font-label text-[9px] uppercase tracking-[0.2em] text-[#C4C6CE] block mb-2">PROBLEM CONTEXT</span>
      <p id="modal-context" class="font-body text-[14px] text-[#1C1B1B] leading-[1.75]"></p>
    </div>

    <div class="border-t-[0.5px] border-[#C4C6CE] pt-6 mb-6 text-left">
      <span class="font-label text-[9px] uppercase tracking-[0.2em] text-[#C4C6CE] block mb-2">OBJECTIVE</span>
      <p id="modal-objective" class="font-body text-[14px] text-[#1C1B1B] leading-[1.75]"></p>
    </div>

    <div class="border-t-[0.5px] border-[#C4C6CE] pt-6 text-left">
      <span class="font-label text-[9px] uppercase tracking-[0.2em] text-[#C4C6CE] block mb-2">ML TASK DEFINITION</span>
      <p id="modal-mltask" class="font-body text-[14px] text-[#1C1B1B] leading-[1.75]"></p>
    </div>
  </div>
</div>

<script>
  const problemDetails = [
    {
      cat: "DIABETIC CARE",
      title: "AI-Based Prediction of High-Risk Plantar Pressure Zones",
      ctx: "Diabetic Foot Ulcers (DFUs) are one of the most severe complications of diabetes mellitus. Due to peripheral neuropathy, many diabetic patients lose sensation in their feet and cannot detect injuries or excessive pressure while walking. Chronic abnormal plantar pressure distribution leads to tissue breakdown and ulcer formation. Studies estimate that up to 80% of diabetes-related amputations originate from non-healing foot ulcers.",
      obj: "Develop a machine learning system that predicts high-pressure plantar regions and ulcer risk zones in diabetic patients using gait or plantar pressure data. The system should identify areas of abnormal pressure distribution that could lead to ulcer formation and provide insights that could guide personalized off-loading footwear design.",
      ml: "Primary Task: Supervised Machine Learning — Classification / Risk Prediction. Possible formulations: Pressure hotspot classification (predict high-risk regions), Ulcer risk prediction (predict probability), Plantar pressure map analysis (detect abnormal distributions). Data modalities: Pressure sensor matrices, Gait time-series, Foot images/scans, Biomechanical features."
    },
    {
      cat: "PATIENT MONITORING",
      title: "AI-Based Early Warning System for Patient Physiological Deterioration",
      ctx: "Dependent elderly individuals and patients with neurological conditions are at high risk of silent physiological decline. Early warning signs—such as infection, dehydration, or systemic instability—often appear first through subtle changes in vital signs including heart rate, respiratory rate, temperature, blood pressure, and oxygen saturation. In many cases, these signals are missed or detected too late.",
      obj: "Develop a machine learning model that predicts the risk of patient physiological deterioration within a defined time window (e.g., next 6–12 hours) using historical vital sign measurements. The system should analyze time-series patient data and generate a risk score or classification indicating whether the patient is likely to deteriorate.",
      ml: "Primary ML Task: Time-Series Prediction / Binary Classification. Predict whether a patient will experience clinical deterioration within the next time window based on previous vital signs. Possible targets: ICU transfer, Sepsis onset, Clinical instability, Mortality risk. Approaches: XGBoost/LightGBM, LSTM/GRU, Temporal CNNs, Transformers."
    },
    {
      cat: "BONE HEALTH",
      title: "AI-Based Osteoporosis Risk Screening from Routine X-Ray Radiographs",
      ctx: "Osteoporosis is a chronic skeletal disease characterized by low bone mineral density (BMD) and deterioration of bone structure. The gold standard DEXA scanning is expensive and often inaccessible in low-resource settings. X-ray imaging, however, is widely available. Analyzing routine radiographs (wrist, hip, spine) could enable large-scale early screening using existing infrastructure.",
      obj: "Develop a machine learning model that analyzes bone radiographs and predicts the risk of osteoporosis or low bone mineral density. The system should accept X-ray images, process them using computer vision models, and output a predicted osteoporosis risk score or classification.",
      ml: "Primary Task: Computer Vision — Image Classification. Possible formulations: Binary Classification (Normal/Osteoporosis risk), Multi-class Classification (Normal/Osteopenia/Osteoporosis), or Regression (predict estimated BMD)."
    },
    {
      cat: "REHABILITATION",
      title: "AI-Based Detection of Incorrect Exercise Form Using Human Pose Estimation",
      ctx: "Incorrect exercise form is a leading contributor to musculoskeletal injuries. Poor movement patterns such as joint misalignment or asymmetrical motion place abnormal stress on joints. Advances in computer vision and pose estimation now allow cameras to capture human motion and estimate skeletal joint positions, enabling automated biomechanical analysis without professional supervision.",
      obj: "Develop a machine learning system that analyzes human exercise movements using pose estimation and detects incorrect exercise form or biomechanical abnormalities. Extract pose keypoints from images/videos and analyze joint angles and trajectories.",
      ml: "Primary Task: Computer Vision + Classification. Pipeline: 1. Pose Estimation (Extract joint coordinates), 2. Feature Engineering (Joint angles, symmetry metrics), 3. ML Classification (Correct vs Incorrect form including error categories like knee valgus or insufficient depth)."
    },
    {
      cat: "STROKE",
      title: "AI-Based Infarct Volume Estimation from Non-Contrast CT",
      ctx: "Acute ischemic stroke is a leading cause of disability. Rapid identification of infarct size is critical for treatment decisions like mechanical thrombectomy. Non-contrast CT (NCCT) is widely available but changes can be extremely subtle. An AI system capable of estimating infarct volume from NCCT scans could support faster triage decisions in emergency settings.",
      obj: "Develop a machine learning system that analyzes non-contrast CT brain scans and estimates the ischemic stroke lesion volume in patients with anterior circulation acute ischemic stroke. The system should automatically detect and segment infarct regions.",
      ml: "Primary Task: Medical image segmentation (Pixel/voxel-level infarct mask from NCCT). Secondary Task: Regression/Volume estimation (Compute predicted volume in mL). Optional: Classify size (Small <30mL, Medium 30-70mL, Large >70mL)."
    }
  ];

  let activeIndex = null;
  const cards = document.querySelectorAll('.problem-card');
  const modal = document.getElementById('problem-modal');
  const modalContent = document.getElementById('problem-modal-content');

  cards.forEach((card, index) => {
    card.addEventListener('click', (e) => {
      // Toggle Accordion functionality
      if (activeIndex === index) {
        // close current
        card.querySelector('.accordion-content').classList.add('hidden');
        card.querySelector('.plus-icon').style.transform = 'rotate(0deg)';
        activeIndex = null;
      } else {
        // open current, close previous
        if (activeIndex !== null) {
          cards[activeIndex].querySelector('.accordion-content').classList.add('hidden');
          cards[activeIndex].querySelector('.plus-icon').style.transform = 'rotate(0deg)';
        }
        card.querySelector('.accordion-content').classList.remove('hidden');
        card.querySelector('.plus-icon').style.transform = 'rotate(45deg)';
        activeIndex = index;
      }

      // Open Modal
      document.getElementById('modal-category').innerText = problemDetails[index].cat;
      document.getElementById('modal-title').innerText = problemDetails[index].title;
      document.getElementById('modal-context').innerText = problemDetails[index].ctx;
      document.getElementById('modal-objective').innerText = problemDetails[index].obj;
      document.getElementById('modal-mltask').innerText = problemDetails[index].ml;

      modal.classList.remove('pointer-events-none');
      modal.classList.replace('opacity-0', 'opacity-100');
      
      setTimeout(() => {
        modalContent.style.opacity = '1';
        modalContent.style.transform = 'translateY(0) scale(1)';
      }, 10);
    });
  });

  const closeModal = () => {
    modalContent.style.transitionDuration = '180ms';
    modalContent.style.transform = 'translateY(16px) scale(0.97)';
    modalContent.style.opacity = '0';
    
    setTimeout(() => {
      modal.classList.replace('opacity-100', 'opacity-0');
      modal.classList.add('pointer-events-none');
    }, 180);
  };

  document.getElementById('modal-close').addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('pointer-events-none')) closeModal();
  });
</script>
</body>"""

text = text.replace("</body>", modal_html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Update accomplished!")
