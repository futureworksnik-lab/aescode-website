import re

file_path = "/Users/nikhilgour/Documents/Aescode Co./stitch_aescode_accelerator_site/cohort_1_2026_update/cohort1.html"
with open(file_path, "r") as f:
    content = f.read()

# Replace the marquee tracks
pattern_marquee = r"        <!-- Row 1 -->[\s\S]*?<!-- Row 2 -->[\s\S]*?</div>"
new_marquee = """        <!-- Row 1 -->
        <div class="marquee-track row-1" id="marquee-row-1"></div>

        <!-- Row 2 -->
        <div class="marquee-track row-2" id="marquee-row-2"></div>"""
content = re.sub(pattern_marquee, new_marquee, content, count=1)

# Add the JS config array and function at the top of the script
new_script = """  <script>
    const archiveImages = [
      "archive/event_01.jpeg",
      "archive/event_02.jpeg",
      "archive/event_03.jpeg",
      "archive/event_04.jpeg",
      "archive/event_05.jpeg",
      "archive/event_06.jpeg",
      "archive/event_07.jpeg",
      "archive/event_08.jpeg",
      "archive/event_09.jpeg",
      "archive/event_10.jpeg"
    ];

    function buildMarquee() {
      const row1 = document.getElementById('marquee-row-1');
      const row2 = document.getElementById('marquee-row-2');

      const mid = Math.ceil(archiveImages.length / 2);
      const set1 = archiveImages.slice(0, mid);
      const set2 = archiveImages.slice(mid);

      const loop1 = [...set1, ...set1];
      const loop2 = [...set2, ...set2];

      function createCard(src) {
        const div = document.createElement('div');
        div.className = 'w-[280px] h-[200px] shrink-0 rounded-[8px] overflow-hidden';
        div.style.marginRight = '16px';
        const img = document.createElement('img');
        img.src = src;
        img.alt = 'AesCode Cohort 1 Archive';
        img.className = 'w-full h-full object-cover';
        img.loading = 'lazy';
        div.appendChild(img);
        return div;
      }

      loop1.forEach(src => row1.appendChild(createCard(src)));
      loop2.forEach(src => row2.appendChild(createCard(src)));
    }

    document.addEventListener('DOMContentLoaded', buildMarquee);

    const problemDetails = ["""

content = content.replace("  <script>\n    const problemDetails = [", new_script)

with open(file_path, "w") as f:
    f.write(content)
print("Done")
