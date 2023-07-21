class elem ():
#CUSTOMER
    #login
    custBtn = "/html/body/div/div/div[2]/div/div[1]/div[1]/button"
    clName = "/html/body/div/div/div[2]/div/form/div/select/option[3]" 
    clName1 = "/html/body/div/div/div[2]/div/form/div/select/option[2]"
    loginBtn = "/html/body/div/div/div[2]/div/form/button"
    #account number
    acNumber ="/html/body/div/div/div[2]/div/div[1]/select/option[3]"
    valNumber = "/html/body/div/div/div[2]/div/div[2]/strong[3]"
    #transaction
    transBtn = "/html/body/div/div/div[2]/div/div[3]/button[1]"
    bckBtn ="/html/body/div/div/div[2]/div/div[1]/button[1]"
    rstBtn = "/html/body/div/div/div[2]/div/div[1]/button[2]"
    #deposit
    dptBtn = "/html/body/div/div/div[2]/div/div[3]/button[2]"
    dscDpt = "/html/body/div/div/div[2]/div/div[4]/div/form/div/label"
    fromDpt = "/html/body/div/div/div[2]/div/div[4]/div/form/div/input"
    sbdptBtn = "/html/body/div/div/div[2]/div/div[4]/div/form/button"
    valDpt = "/html/body/div/div/div[2]/div/div[4]/div/span"
    #withdrawn
    wdrBtn = "/html/body/div/div/div[2]/div/div[3]/button[3]"
    dscWdr = "/html/body/div/div/div[2]/div/div[4]/div/form/div/label"
    formWdr = "/html/body/div/div/div[2]/div/div[4]/div/form/div/input"
    swdrBtn = "/html/body/div/div/div[2]/div/div[4]/div/form/button"
    valWdr = " /html/body/div/div/div[2]/div/div[4]/div/span"
    valWdr1 = "/html/body/div/div/div[2]/div/div[4]/div/span"
    #logout
    logBtn = "/html/body/div/div/div[1]/button[2]"
    homeBtn ="/html/body/div/div/div[1]/button[1]"

#BANK MANAGER
    #add customer
    mngBtn = "/html/body/div/div/div[2]/div/div[1]/div[2]/button"
    addBtn = "/html/body/div/div/div[2]/div/div[1]/button[1]"
    inpFirst = "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input"
    inpLast = "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input"
    inpPost = "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input"
    addBtn1 = "//html/body/div/div/div[2]/div/div[2]/div/div/form/button"
    #open account
    accBtn ="/html/body/div/div/div[2]/div/div[1]/button[2]"
    inpCust = "/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/select/option[2]"
    inpCurr ="/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/select/option[2]"
    proBtn = "/html/body/div/div/div[2]/div/div[2]/div/div/form/button"
    #customers
    custsBtn = "/html/body/div/div/div[2]/div/div[1]/button[3]"
    delBtn ="/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[1]/td[5]/button"

class url():
    baseUrl = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    customerUrl = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/customer"
    dashboarUrl = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/account"
    transUrl ="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/listTx"
    managUrl ="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
    accUrl = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount"
    addUrl = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust"
    clistUrl ="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"



