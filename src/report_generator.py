from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


def generate_report(
    business_score,
    demand,
    stockout_risk,
    overstock_risk,
    recommendation,
    output_file="Business_Report.pdf"
):

    doc = SimpleDocTemplate(
        output_file,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontSize=22,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "HeadingCustom",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10
    )

    body_style = ParagraphStyle(
        "BodyCustom",
        parent=styles["BodyText"],
        fontSize=10,
        leading=15
    )

    story = []

    story.append(
        Paragraph(
            "Retail AI Control Tower",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Executive Business Intelligence Report",
            styles["Heading3"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Business Health",
            heading_style
        )
    )

    health_data = [
        ["Metric", "Value"],
        ["Business Score", f"{business_score}/100"],
        ["Predicted Demand", f"{demand:.0f}"],
        ["Stockout Risk", f"{stockout_risk:.1f}%"],
        ["Overstock Risk", f"{overstock_risk:.1f}%"],
    ]

    health_table = Table(
        health_data,
        colWidths=[250, 180]
    )

    health_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563EB")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("PADDING", (0, 0), (-1, -1), 8),
        ])
    )

    story.append(health_table)

    story.append(
        Paragraph(
            "AI Recommendation",
            heading_style
        )
    )

    story.append(
        Paragraph(
            str(recommendation),
            body_style
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Executive Interpretation",
            heading_style
        )
    )

    interpretation = (
        f"The current business health score is {business_score}/100. "
        f"Predicted demand is approximately {demand:.0f} units. "
        f"The model identifies a stockout risk of {stockout_risk:.1f}% "
        f"and an overstock risk of {overstock_risk:.1f}%. "
        "These indicators should be considered together when making "
        "pricing and inventory decisions."
    )

    story.append(
        Paragraph(
            interpretation,
            body_style
        )
    )

    story.append(Spacer(1, 25))

    story.append(
        Paragraph(
            "Retail AI Control Tower | AI for Business Portfolio",
            styles["BodyText"]
        )
    )

    doc.build(story)

    return output_file