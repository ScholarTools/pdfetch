from pdfetch.pdfetch_errors import *

def get_pdf(paper_info):
    try:
        if paper_info.publisher_interface is None:
            paper_info.make_interface_object()
        pdf_content = paper_info.publisher_interface.get_pdf_content(pdf_url=paper_info.pdf_link)
    except Exception:
        raise PDFError('PDF could not be retrieved')

    if pdf_content is None:
        raise PDFError('PDF could not be retrieved')

    return pdf_content
