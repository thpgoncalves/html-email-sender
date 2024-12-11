from email_service.gmail_email_service import authenticate_email_service, send_email_message

def send_email(details):
    """Envia um email formatado baseado nos dados recebidos."""
    service = authenticate_email_service()
    sender_email = "example_sender@gmail.com"  
    recipient_email = "example_recipient@example.com"  
    subject = "Example Email with Email API"
    message = f"""
        <!DOCTYPE html>
        <html>
        <body>
            <table width="100%" cellpadding="24px" cellspacing="0" style="background-color:#f7f9fa;padding:24px">
                <table width="100%" cellpadding="0" cellspacing="0" style="text-align: center;background-color:#ffffff;padding: 24px;">
                    <tbody>
                        <tr>
                            <td>
                                <table cellpadding="0" cellspacing="0" width="100%">
                                    <tbody>
                                        <tr>
                                            <td style="vertical-align:middle; text-align: center;">
                                                <a style="color:#1c1d1f;">
                                                    Hello {details['contact']}, how are you?
                                                </a>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="border-top:1px solid #cccccc;padding: 24px 200px 0px 200px; text-align: justify">
                                <p>We are reaching out regarding item N°{details['item']} of the PO {details['sales_doc']}.</p>
                                <p>We are currently facing a delay in the production of material {details['brand']}-{details['material']}
                                and would like to suggest a substitute to meet your order's needs.</p>
                                <p>Your order's item is {details['brand']}-{details['material']} and the suggested substitute is
                                {details['brand']}-{details['replacement_material']}.</p>
                                <p style="text-align: center;">Below, we show the visual color difference between the requested item and the suggested item:</p>
                            </td>
                        </tr>
                    </tbody>
                    <table width="80%" cellpadding="0" cellspacing="5px" style="align: center;">
                        <tr>
                            <td style="background-color: rgb({details['R']}, {details['G']}, {details['B']}); height: 50px; width: 50%; text-align: center; vetical-align: middle; border: 2px solid black;">
                            {details['brand']}-{details['material']}
                            </td>
                            <td style="background-color: rgb({details['R_replacement']}, {details['G_replacement']}, {details['B_replacement']}); height: 50px; width: 50%; text-align: center; vetical-align: middle; border: 2px solid black;">
                            {details['brand']}-{details['replacement_material']}
                            </td>
                        </tr>
                    </table>
                </table>
            </table>
        </body>
        </html>
        """
    send_email_message(service, sender_email, recipient_email, subject, message)