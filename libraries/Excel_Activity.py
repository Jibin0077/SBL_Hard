
# -
# def lib_append_to_Data_list(Ext_Title,Ext_Author,Ext_Publ_date,Ext_Publisher,Ext_Collection,Ext_Contributor,Ext_Identifier):

#     list_details=[]
#     #if Code1!=None and Code2!=None:
#     list_details.extend([Ext_Title,Ext_Author,Ext_Publ_date,Ext_Publisher,Ext_Collection,Ext_Contributor,Ext_Identifier])
#     #else:

#         #list_details.extend([Client,InvoiceNumber,Insurance,PTname,DOS,ServiceCode,MPI,CCN_Number,RemitDate,DEB,PaidAmount,Status,HCPCS_Code,str(FromDate),str(NumServices),SubmittedAmount,AllowedAmount])
#     return list_details
#--------------------------------------------------
# -Ext_Author,Ext_Publ_date,Ext_Publisher,Ext_Collection,Ext_Contributor,Ext_Identifier,Ext_Copyright,Ext_pdf_name):
#,Ext_Author,Ext_Publ_date,Ext_Publisher,Ext_Collection,Ext_Contributor,Ext_Identifier,Ext_Copyright,Ext_pdf_name])
def lib_append_to_Data_list(Ext_Title,Ext_Author,Ext_Publ_date,Ext_Publisher,Ext_Collection,Ext_Contributor,Ext_Identifier,Ext_Copyright,Ext_pdf_name):

    list_details=[]
    #if Code1!=None and Code2!=None:
    list_details.extend([Ext_Title,Ext_Author,Ext_Publ_date,Ext_Publisher,Ext_Collection,Ext_Contributor,Ext_Identifier,Ext_Copyright,Ext_pdf_name])
    #else:

        #list_details.extend([Client,InvoiceNumber,Insurance,PTname,DOS,ServiceCode,MPI,CCN_Number,RemitDate,DEB,PaidAmount,Status,HCPCS_Code,str(FromDate),str(NumServices),SubmittedAmount,AllowedAmount])
    return list_details

#-------------------------------------------------------

# +
from csv import writer

def Write_phm_Output(saveloc,List):  
    
    with open(saveloc+'\Internet_Archive_out.csv','a',newline='') as f_object:
# Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
# Pass the list as an argument into
        # the writerow()
        # -----------------------------
        # List = "|".join(List)
        #--------------------------------------
        writer_object.writerow(List)
#Close the file object
        f_object.close()
