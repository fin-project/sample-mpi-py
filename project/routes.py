from project.key import Key
from project.mpi import MPI
from project.forms import MpiForm
from flask import render_template, request, Response
from datetime import datetime
from project import app

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('Checkout.html', title="Hosted Payment Page")

# ---------------------
# MPI Webhook
# ---------------------

@app.route('/mpi_status', methods=['POST','GET'])
def mpi_status():

    result="OK"
    return Response(result, status=200)


@app.route('/mpi_redirect', methods=['POST', 'GET'])
def mpi_redirect():

    print("---header---")
    print(request.headers)
    
    print("------data------")
    appr_code = request.form.get('MPI_APPR_CODE',"")
    rrn = request.form.get('MPI_RRN',"")
    bin = request.form.get('MPI_BIN',"")
    error_code = request.form.get('MPI_ERROR_CODE',"")
    error_desc = request.form.get('MPI_ERROR_DESC',"")
    merc_id = request.form.get('MPI_MERC_ID',"")
    trxn_id = request.form.get('MPI_TRXN_ID',"")
    mac = request.form.get('MPI_MAC',"")
    referral_code = request.form.get('MPI_REFERRAL_CODE',"")    
    
    # Additional data
    eci = request.form.get('MPI_ECI_VALUE',"")    
    challenge_mandated_ind = request.form.get('MPI_CHALLENGE_MANDATED_IND',"")    
    challenge_ind = request.form.get('MPI_CHALLENGE_IND',"")    
    auth_status = request.form.get('MPI_AUTH_STATUS',"")   
    status_reason = request.form.get('MPI_STATUS_REASON',"")   
    status_reason_desc = request.form.get('MPI_STATUS_REASON_DESC',"")
  
    #return Response(result, status=200)
    return render_template('MpiResult.html', appr_code = appr_code, rrn = rrn, bin = bin, 
        error_code = error_code, error_desc = error_desc, merc_id = merc_id, trxn_id = trxn_id, 
        referral_code = referral_code,
        eci = eci, challenge_mandated_ind = challenge_mandated_ind, challenge_ind = challenge_ind,
        status_reason = status_reason, status_reason_desc = status_reason_desc
        )

# ---------------------
# MPI 
# ---------------------

@app.route('/checkout')
def checkout():
    return render_template('Checkout.html')

@app.route('/checkout_iframe', methods=['GET','POST'])
def checkout_iframe():
    form = MpiForm()

    now = datetime.now().strftime("%Y%m%d%H%M%S")

    # Load default value
    form.MPI_TRANS_TYPE.data 	= "SALES"
    form.MPI_MERC_ID.data       = app.config["TEST_MID"]
    form.MPI_TRXN_ID.data       = app.config["TEST_APP_KEY"] + now
    form.MPI_PURCH_DATE.data 	= now
    form.MPI_PURCH_CURR.data 	= "458"
    form.MPI_PURCH_AMT.data 	= "100"
    form.MPI_ADDR_MATCH.data 	= "N"

    return render_template('CheckoutIframe.html', form=form)


@app.route('/sign_data', methods=['GET','POST'])
def sign_data():

    print("---header---")
    print(request.headers)
    
    print("------data------")
    print(request.form)
    
    trans_type = request.form.get('MPI_TRANS_TYPE',"")
    merc_id = request.form.get('MPI_MERC_ID',"")
    pan = request.form.get('MPI_PAN',"")
    cardholder_name = request.form.get('MPI_CARD_HOLDER_NAME',"")
    pan_exp = request.form.get('MPI_PAN_EXP',"")
    cvv2 = request.form.get('MPI_CVV2',"")
    trxn_id = request.form.get('MPI_TRXN_ID',"")
    ori_trxn_id = request.form.get('MPI_ORI_TRXN_ID',"")
    puch_date = request.form.get('MPI_PURCH_DATE',"")
    purch_curr = request.form.get('MPI_PURCH_CURR',"")
    purch_amt = request.form.get('MPI_PURCH_AMT',"")
    addr_match = request.form.get('MPI_ADDR_MATCH',"")
    bill_addr_city = request.form.get('MPI_BILL_ADDR_CITY',"")
    bill_addr_state = request.form.get('MPI_BILL_ADDR_STATE',"")
    bill_addr_cntry = request.form.get('MPI_BILL_ADDR_CNTRY',"")
    bill_addr_postcode = request.form.get('MPI_BILL_ADDR_POSTCODE',"")
    bill_addr_line1 = request.form.get('MPI_BILL_ADDR_LINE1',"")
    bill_addr_line2 = request.form.get('MPI_BILL_ADDR_LINE2',"")
    bill_addr_line3 = request.form.get('MPI_BILL_ADDR_LINE3',"")
    ship_addr_cty = request.form.get('MPI_SHIP_ADDR_CITY',"")
    ship_addr_state = request.form.get('MPI_SHIP_ADDR_STATE',"")
    ship_addr_cntry = request.form.get('MPI_SHIP_ADDR_CNTRY',"")
    ship_addr_postcode = request.form.get('MPI_SHIP_ADDR_POSTCODE',"")
    ship_addr_line1 = request.form.get('MPI_SHIP_ADDR_LINE1',"")
    ship_addr_line2 = request.form.get('MPI_SHIP_ADDR_LINE2',"")
    ship_addr_line3 = request.form.get('MPI_SHIP_ADDR_LINE3',"")
    email = request.form.get('MPI_EMAIL',"")
    home_phone = request.form.get('MPI_HOME_PHONE',"")
    home_phone_cc = request.form.get('MPI_HOME_PHONE_CC',"")
    work_phone = request.form.get('MPI_WORK_PHONE',"")
    work_phone_cc = request.form.get('MPI_WORK_PHONE_CC',"")
    mobile_phone = request.form.get('MPI_MOBILE_PHONE',"")
    mobile_phone_cc = request.form.get('MPI_MOBILE_PHONE_CC',"")
    response_type = request.form.get('MPI_RESPONSE_TYPE',"")
    additional_info_ind = request.form.get('MPI_ADDITIONAL_INFO_IND',"")
    recurring_frequency = request.form.get('MPI_RECURR_FREQ',"")
    recurring_expiry = request.form.get('MPI_RECURR_EXPIRY',"")
    instal_data = request.form.get('MPI_RECURR_MAX_CNT',"")
    recurring_max_amt = request.form.get('MPI_RECURR_MAX_AMT',"")
    recurring_total_amt = request.form.get('MPI_RECURR_MAX_TOTAL',"")
    
    data = trans_type+merc_id+pan+cardholder_name+pan_exp+cvv2+trxn_id+ori_trxn_id+puch_date
    data = data+purch_curr+purch_amt+addr_match+bill_addr_city+bill_addr_state+bill_addr_cntry
    data = data+bill_addr_postcode+bill_addr_line1+bill_addr_line2+bill_addr_line3+ship_addr_cty
    data = data+ship_addr_state+ship_addr_cntry+ship_addr_postcode+ship_addr_line1+ship_addr_line2
    data = data+ship_addr_line3+email+home_phone+home_phone_cc+work_phone+work_phone_cc+mobile_phone
    data = data+mobile_phone_cc+response_type+additional_info_ind+recurring_frequency+recurring_expiry
    data = data+instal_data+recurring_max_amt+recurring_total_amt
    #print(data)

    if trxn_id != "":
        id = trxn_id
    else:
        id = ori_trxn_id

    m = MPI(merc_id, id)
    return m.KeySign(data)


