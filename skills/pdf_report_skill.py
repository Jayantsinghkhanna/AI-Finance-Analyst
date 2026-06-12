from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import os


def pdf_report_skill(state):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    ticker = state.get(
        "ticker",
        "REPORT"
    )

    pdf_path = (
        f"reports/{ticker}_Investment_Report.pdf"
    )

    doc = SimpleDocTemplate(
        pdf_path
    )

    styles = (
        getSampleStyleSheet()
    )

    content = []

    title = Paragraph(
        f"{ticker} Investment Report",
        styles["Title"]
    )

    content.append(title)

    content.append(
        Spacer(
            1,
            20
        )
    )

    report_text = (
        state["final_report"]
    )

    paragraphs = (
        report_text.split("\n")
    )

    for line in paragraphs:

        if line.strip():

            content.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(
                    1,
                    5
                )
            )

    doc.build(content)

    state["pdf_path"] = (
        pdf_path
    )

    print(
        f"\nPDF GENERATED -> {pdf_path}"
    )

    return state