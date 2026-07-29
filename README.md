<svg width="1200" height="300" viewBox="0 0 1200 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background -->
    <linearGradient id="bgGrad-light" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f6f8fa"/>
    </linearGradient>

    <!-- Accent gradient for line + cursor, slowly cycling hue -->
    <linearGradient id="accentGrad-light" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0969da">
        <animate attributeName="stop-color"
          values="#0969da;#8250df;#1a7f37;#0969da"
          dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#8250df">
        <animate attributeName="stop-color"
          values="#8250df;#1a7f37;#0969da;#8250df"
          dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#1a7f37">
        <animate attributeName="stop-color"
          values="#1a7f37;#0969da;#8250df;#1a7f37"
          dur="8s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <!-- Clip path for typewriter title reveal -->
    <clipPath id="titleClip-light">
      <rect x="0" y="0" height="120" width="0">
        <animate attributeName="width" from="0" to="900"
          begin="0.3s" dur="1.8s" fill="freeze" calcMode="spline"
          keySplines="0.25 0.1 0.25 1"/>
      </rect>
    </clipPath>
  </defs>

  <!-- Background -->
  <rect width="1200" height="300" fill="url(#bgGrad-light)"/>

  <!-- Floating decorative dots -->
  <circle cx="1080" cy="70" r="5" fill="#0969da" opacity="0.5">
    <animate attributeName="cy" values="70;50;70" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.5;0.12;0.5" dur="4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="1130" cy="130" r="3.5" fill="#8250df" opacity="0.45">
    <animate attributeName="cy" values="130;105;130" dur="5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.45;0.1;0.45" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="1000" cy="220" r="4" fill="#1a7f37" opacity="0.45">
    <animate attributeName="cy" values="220;195;220" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.45;0.1;0.45" dur="6s" repeatCount="indefinite"/>
  </circle>
  <circle cx="60" cy="240" r="4.5" fill="#0969da" opacity="0.35">
    <animate attributeName="cx" values="60;90;60" dur="7s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.35;0.08;0.35" dur="7s" repeatCount="indefinite"/>
  </circle>

  <!-- Title: typewriter reveal via clip-path -->
  <!-- EDIT THIS TEXT: replace "YOUR PROJECT NAME" with your repo name -->
  <g clip-path="url(#titleClip-light)">
    <text x="80" y="150" font-family="'Segoe UI', Helvetica, Arial, sans-serif"
          font-size="52" font-weight="700" fill="#24292f">Hi, I'm Shivam Mishra 👋</text>
  </g>

  <!-- Blinking cursor while title is being "typed", then hides -->
  <rect x="770" y="102" width="6" height="52" fill="url(#accentGrad-light)" opacity="0">
    <animate attributeName="opacity" values="1;0;1;0;1;0;1;0;1;0"
      begin="0.3s" dur="1.8s" fill="freeze"/>
    <set attributeName="opacity" to="0" begin="2.1s"/>
  </rect>

  <!-- Tagline: fades in after title finishes typing -->
  <text x="82" y="200" font-family="'Segoe UI', Helvetica, Arial, sans-serif"
        font-size="24" font-weight="400" fill="#57606a" opacity="0">
    Full Stack Developer (MERN) · Building End-to-End Applications
    <animate attributeName="opacity" from="0" to="1" begin="2.1s" dur="1s" fill="freeze"/>
  </text>

  <!-- Animated accent line, drawing in under the tagline -->
  <line x1="82" y1="225" x2="82" y2="225" stroke="url(#accentGrad-light)" stroke-width="4" stroke-linecap="round">
    <animate attributeName="x2" from="82" to="700" begin="2.3s" dur="1.2s"
      calcMode="spline" keySplines="0.25 0.1 0.25 1" fill="freeze"/>
  </line>
</svg>
