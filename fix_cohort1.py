import re

with open('/Users/nikhilgour/Documents/Aescode Co./stitch_aescode_accelerator_site/cohort_1_2026_update/cohort1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change 1: Section Side Headings
# These are h2 elements with sticky top-32
html = re.sub(
    r'<h2 class="font-label text-\[10px\] tracking-\[0\.2em\] uppercase text-(primary|\[#707785\]) sticky top-32"',
    r'<h2 class="font-label font-medium text-[11px] tracking-[0.2em] uppercase text-[#021934] sticky top-32"',
    html
)

# Change 2: Timeline Dates
html = html.replace(
    'class="col-span-1 font-label text-[10px] tracking-widest uppercase text-outline"',
    'class="col-span-1 font-label font-medium text-[11px] tracking-widest uppercase text-[#021934]"'
)

# Change 3: Problem Accordion Cards
html = html.replace(
    'class="problem-card group text-left w-full bg-[#FFFFFF] rounded-[2px] border-t-[0.5px] border-[#C4C6CE] py-6 hover:bg-[#FCF9F8] transition-colors"',
    'class="problem-card group text-left w-full bg-[#FAFAF9] rounded-[6px] border-t-[0.5px] border-[#C4C6CE] py-8 mb-3 hover:bg-[#F5F3F2] transition-colors"'
)
html = html.replace('<div id="accordion-container" class="flex flex-col">', '<div id="accordion-container" class="flex flex-col border-b-[0.5px] border-[#C4C6CE]">')

# Change 4: Judges - Image Hover
html = html.replace(
    'class="w-full aspect-[4/5] object-cover rounded-[2px] grayscale"',
    'class="w-full aspect-[4/5] object-cover rounded-[2px] grayscale hover:grayscale-0 transition-all duration-500 ease-in-out"'
)

# Change 5: Mentors Section
html = html.replace(
    'class="shrink-0 w-[80px] h-[100px]"',
    'class="shrink-0 w-[120px] h-[150px]"'
)
html = html.replace(
    'class="w-full h-full object-cover rounded-[2px] grayscale"',
    'class="w-full h-full object-cover rounded-[2px] grayscale hover:grayscale-0 transition-all duration-500 ease-in-out"'
)
# Make sure we only change the gap-8 and py-[32px] for Mentors. 
# Mentors are the only ones with border-t-[0.5px] border-[#C4C6CE] py-[32px] gap-8
html = html.replace(
    'class="flex gap-8 border-t-[0.5px] border-[#C4C6CE] py-[32px]"',
    'class="flex gap-10 border-t-[0.5px] border-[#C4C6CE] py-[40px]"'
)
html = html.replace(
    '<h4 class="font-headline text-[22px] text-[#021934] font-normal">Mr. Viraj Gaur</h4>',
    '<h4 class="font-headline text-[24px] text-[#021934] font-normal">Mr. Viraj Gaur</h4>'
)
html = html.replace(
    '<h4 class="font-headline text-[22px] text-[#021934] font-normal">Dr. Subham Ghosh</h4>',
    '<h4 class="font-headline text-[24px] text-[#021934] font-normal">Dr. Subham Ghosh</h4>'
)
html = html.replace(
    '<h4 class="font-headline text-[22px] text-[#021934] font-normal">Mr. Shayantan Banerjee</h4>',
    '<h4 class="font-headline text-[24px] text-[#021934] font-normal">Mr. Shayantan Banerjee</h4>'
)

# For 5F: Mentors background shift
# The mentors section is <!-- 07. Mentors --> \n <section class="mb-48">
html = html.replace(
    '<!-- 07. Mentors -->\n    <section class="mb-48">',
    '<!-- 07. Mentors -->\n    <section class="mb-48 py-16 bg-[#F6F3F2] -mx-8 px-8">'
)

# Change 6: Footer Standardization
# 6A
html = html.replace(
    '<footer class="bg-[#FCF9F8] dark:bg-slate-950 border-t-[0.5px] border-slate-300 dark:border-slate-800 py-12">',
    '<footer class="bg-[#FCF9F8] py-12">'
)
# 6B
html = html.replace(
    '<div class="font-serif text-xl text-[#021934] dark:text-slate-100" style="">AesCode Co.</div>',
    '<div class="font-label font-bold text-[13px] tracking-[0.08em] uppercase text-[#021934]">AesCode Co.</div>'
)
# 6C
tagline_old = '<p class="font-headline italic text-on-surface-variant text-sm" style=""><span\n            style="color: rgb(100, 116, 139); font-family: Newsreader, serif;" class="">MedTech Research. Clinically\n            Grounded. Institutionally Anchored.</span></p>'
tagline_new = '<p class="font-headline italic text-[13px] text-[#707785]">\n          MedTech Research. Clinically Grounded. Institutionally Anchored.</p>'
# Use regex for tagline due to formatting
html = re.sub(
    r'<p class="font-headline italic text-on-surface-variant text-sm"[^>]*>.*?MedTech Research.*?Anchored\.</span></p>',
    r'<p class="font-headline italic text-[13px] text-[#707785]">\n          MedTech Research. Clinically Grounded. Institutionally Anchored.</p>',
    html,
    flags=re.DOTALL
)

# 6D
html = html.replace(
    'class="text-slate-500 dark:text-slate-400 Labels: Public Sans text-[10px] tracking-widest uppercase underline decoration-slate-300 underline-offset-4"',
    'class="font-label text-[10px] tracking-[0.2em] uppercase text-[#707785] hover:text-[#021934] transition-colors duration-200"'
)
html = html.replace(
    'href="#" style="">Privacy Policy</a>',
    'href="#">Privacy Policy</a>'
)
html = html.replace(
    'href="#" style="">Terms of Service</a>',
    'href="#">Terms of Service</a>'
)
html = html.replace(
    'href="#" style="">Archive</a>',
    'href="#">Archive</a>'
)
html = html.replace(
    'href="#" style="">RSS</a>',
    'href="#">RSS</a>'
)

# 6E
html = html.replace(
    'class="Labels: Public Sans text-[10px] tracking-widest uppercase text-[#021934] dark:text-white font-bold"\n          style=""',
    'class="font-label font-medium text-[10px] tracking-[0.2em] uppercase text-[#021934]"'
)
# Single line version just in case
html = html.replace(
    'class="Labels: Public Sans text-[10px] tracking-widest uppercase text-[#021934] dark:text-white font-bold" style=""',
    'class="font-label font-medium text-[10px] tracking-[0.2em] uppercase text-[#021934]"'
)

# 6F
html = html.replace(
    'class="text-[10px] text-outline font-label uppercase tracking-tighter mt-4 md:mt-0"\n          style=""',
    'class="font-label text-[10px] uppercase tracking-[0.2em] text-[#C4C6CE] mt-4 md:mt-0"'
)
html = html.replace(
    'class="text-[10px] text-outline font-label uppercase tracking-tighter mt-4 md:mt-0" style=""',
    'class="font-label text-[10px] uppercase tracking-[0.2em] text-[#C4C6CE] mt-4 md:mt-0"'
)

with open('/Users/nikhilgour/Documents/Aescode Co./stitch_aescode_accelerator_site/cohort_1_2026_update/cohort1.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
