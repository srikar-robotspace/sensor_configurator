STYLESHEET = """

QWidget {
    background-color: #0d1117;
    color: #e6edf3;
    font-family: "Inter", "Segoe UI", sans-serif;
    font-size: 13px;
}

QFrame#card {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
}

QLabel#card_eyebrow {
    color: #6e7681;
    font-size: 10px;
    font-weight: bold;
    letter-spacing: 1.4px;
}

QLabel#mono_large {
    font-family: "JetBrains Mono";
    font-size: 22px;
    font-weight: 600;
    color: #00d4ff;
}

QLabel#sub {
    color: #6e7681;
    font-size: 12px;
}

QLabel#hint {
    color: #484f58;
    font-size: 11px;
    font-style: italic;
}

QLabel#title {
    font-size: 18px;
    font-weight: 700;
    color: #e6edf3;
}

QLabel#badge {
    background-color: #1f2937;
    border: 1px solid #374151;
    border-radius: 4px;
    color: #6ee7b7;
    font-size: 10px;
    font-weight: bold;
    padding: 3px 8px;
}

QPushButton#primary_btn {
    background-color: #0d47a1;
    color: #e6edf3;
    border: 1px solid #1565c0;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
}

QPushButton#primary_btn:hover {
    background-color: #1565c0;
    border-color: #00d4ff;
}

QPushButton#assign_btn {
    background-color: #14532d;
    color: #86efac;
    border: 1px solid #166534;
    border-radius: 8px;
    font-weight: 600;
    font-size: 13px;
}

QPushButton#assign_btn:hover {
    background-color: #166534;
}

QPushButton#ghost_btn {
    background-color: transparent;
    color: #6e7681;
    border: 1px solid #30363d;
    border-radius: 5px;
}

QLineEdit#addr_input {
    background-color: #0d1117;
    border: 1px solid #30363d;
    border-radius: 8px;
    color: #e6edf3;
    font-size: 15px;
    padding: 0 14px;
}

QLineEdit#addr_input:focus {
    border-color: #00d4ff;
}

QTextEdit#log {
    background-color: #0d1117;
    border: 1px solid #21262d;
    border-radius: 6px;
    color: #8b949e;
    font-family: "JetBrains Mono";
    font-size: 12px;
}
"""