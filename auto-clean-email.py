import win32com.client  
[att.SaveAsFile(f"C:/invoices/{att.FileName}") for att in win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI").Folders.Item("Inbox").Items if att.Attachments.Count]
