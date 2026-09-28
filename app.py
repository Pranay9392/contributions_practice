def inject_custom_styles(theme_name: str):
    t = THEMES[theme_name]
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Manrope:wght@600;700;800&display=swap');

    :root {{
        --bg: {t["bg"]}; --bg2: {t["bg2"]}; --surface: {t["surface"]};
        --surface2: {t["surface2"]}; --border: {t["border"]};
        --text: {t["text"]}; --muted: {t["muted"]}; --accent: {t["accent"]};
        --accent2: {t["accent2"]}; --soft: {t["soft"]}; --shadow: {t["shadow"]};
        --danger: {t["danger"]}; --warning: {t["warning"]};
    }}

    html, body, [class*="css"] {{ font-family: 'DM Sans', sans-serif; }}
    .stApp {{
        background:
          radial-gradient(circle at 4% 0%, rgba(34,197,94,.15), transparent 27%),
          radial-gradient(circle at 94% 8%, rgba(74,222,128,.09), transparent 24%),
          linear-gradient(135deg, var(--bg), var(--bg2));
        color: var(--text);
    }}
    .main .block-container {{ max-width: 1540px; padding: 1.4rem 2rem 3rem; }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, var(--surface2), var(--bg)) !important;
        border-right: 1px solid var(--border) !important;
        backdrop-filter: blur(18px);
    }}
    section[data-testid="stSidebar"] .block-container {{ padding: 1.1rem .9rem; }}

    .brand {{
        display:flex; align-items:center; gap:.75rem; padding:.45rem .45rem 1.25rem;
    }}
    .brand-mark {{
        width:42px;height:42px;border-radius:13px;display:flex;align-items:center;justify-content:center;
        color:#052e16;font-weight:900;font-size:1.2rem;
        background:linear-gradient(145deg,#86efac,#22c55e);
        box-shadow:0 8px 25px rgba(34,197,94,.28);
    }}
    .brand-title {{ font-family:'Manrope'; font-size:1.05rem; font-weight:800; color:var(--text); }}
    .brand-sub {{ color:var(--accent); font-size:.62rem; font-weight:800; letter-spacing:.13em; }}

    .hero {{
        position:relative; overflow:hidden; margin-bottom:1.2rem; padding:1.65rem 1.7rem;
        border:1px solid var(--border); border-radius:24px;
        background:
          radial-gradient(circle at 90% 15%, rgba(74,222,128,.16), transparent 28%),
          linear-gradient(135deg, var(--surface), rgba(34,197,94,.04));
        box-shadow:0 20px 60px var(--shadow);
        backdrop-filter:blur(20px);
    }}
    .hero:after {{
        content:""; position:absolute; width:170px;height:170px;right:-75px;bottom:-90px;
        border-radius:50%; background:rgba(74,222,128,.08); filter:blur(2px);
    }}
    .hero-kicker {{ color:var(--accent); font-size:.68rem; font-weight:800; letter-spacing:.16em; }}
    .hero h1 {{ margin:.25rem 0 .35rem; color:var(--text); font-family:'Manrope'; font-size:2.05rem; letter-spacing:-.045em; }}
    .hero p {{ margin:0; color:var(--muted); font-size:.9rem; }}

    .metric-card {{
        min-height:122px; padding:1.05rem 1.15rem; border-radius:18px;
        border:1px solid var(--border);
        background:linear-gradient(145deg, var(--surface), rgba(34,197,94,.035));
        box-shadow:0 12px 34px var(--shadow); backdrop-filter:blur(14px);
        position:relative; overflow:hidden;
    }}
    .metric-card:before {{
        content:""; position:absolute; top:0; left:0; right:0; height:2px;
        background:linear-gradient(90deg,transparent,var(--accent),transparent); opacity:.75;
    }}
    .metric-title {{ color:var(--muted); text-transform:uppercase; font-size:.64rem; font-weight:800; letter-spacing:.1em; }}
    .metric-value {{ color:var(--accent) !important; font-family:'Manrope'; font-size:1.9rem; font-weight:800; line-height:1.15; margin-top:.35rem; }}
    .metric-subtitle {{ color:var(--muted); font-size:.7rem; margin-top:.3rem; }}

    .panel {{
        padding:1.1rem 1.15rem; margin-bottom:1rem; border-radius:19px;
        border:1px solid var(--border); background:var(--surface);
        box-shadow:0 12px 38px var(--shadow); backdrop-filter:blur(16px);
    }}
    .panel-title {{ color:var(--text); font-family:'Manrope'; font-size:.98rem; font-weight:800; }}
    .panel-subtitle {{ color:var(--muted); font-size:.71rem; margin:.15rem 0 .75rem; }}
    .section-title {{ color:var(--text); font-family:'Manrope'; font-size:1.05rem; font-weight:800; margin:1.25rem 0 .7rem; }}

    .alert-row {{
        border:1px solid var(--border); border-left:3px solid var(--accent);
        border-radius:13px; padding:.7rem .8rem; margin:.45rem 0;
        background:rgba(34,197,94,.035);
    }}
    .alert-title {{ color:var(--text); font-size:.8rem; font-weight:700; }}
    .alert-meta {{ color:var(--muted); font-size:.68rem; margin-top:.15rem; }}

    .status-pill {{ display:inline-block; padding:.22rem .5rem; border-radius:999px; font-size:.62rem; font-weight:800; }}
    .pill-success {{ color:#166534; background:#DCFCE7; }}
    .pill-warning {{ color:#92400E; background:#FEF3C7; }}
    .pill-danger {{ color:#9F1239; background:#FFE4E6; }}
    .pill-info {{ color:#166534; background:#DCFCE7; }}
    .pill-neutral {{ color:var(--muted); background:rgba(134,168,147,.12); }}

    .insight {{
        border:1px solid var(--border); border-radius:15px; padding:.9rem 1rem;
        background:linear-gradient(120deg,rgba(34,197,94,.07),transparent);
        margin-bottom:.6rem;
    }}
    .insight b {{ color:var(--text); }} .insight span {{ color:var(--muted); font-size:.73rem; }}

    .stButton > button {{
        border:1px solid var(--border); border-radius:11px; font-weight:800;
        background:linear-gradient(135deg,rgba(34,197,94,.10),rgba(34,197,94,.03));
        color:var(--text); transition:.2s ease;
    }}
    .stButton > button:hover {{
        border-color:var(--accent); color:var(--accent);
        box-shadow:0 8px 25px rgba(34,197,94,.12); transform:translateY(-1px);
    }}
    div[data-testid="stDataFrame"] {{
        border:1px solid var(--border); border-radius:14px; overflow:hidden;
    }}
    div[data-baseweb="select"] > div {{
        border-radius:11px !important; border-color:var(--border) !important;
        background:var(--surface2) !important;
    }}
    .stTextInput input, .stTextArea textarea {{
        border-radius:11px !important; border-color:var(--border) !important;
        background:var(--surface2) !important; color:var(--text) !important;
    }}
    hr {{ border-color:var(--border); }}
    .small-muted {{ color:var(--muted); font-size:.7rem; }}
    .health-dot {{
        display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--accent);
        box-shadow:0 0 0 5px rgba(34,197,94,.10);margin-right:7px;
    }}
    </style>
    """, unsafe_allow_html=True)
