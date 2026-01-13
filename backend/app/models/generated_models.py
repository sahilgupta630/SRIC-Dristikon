from sqlalchemy import Column, Integer, String, DateTime, Date, Float, Numeric, LargeBinary, Boolean, BigInteger, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AadhaarPanLink(Base):
    __tablename__ = 'aadhaar_pan_link'

    sl_no = Column(Integer, primary_key=True)
    pan_no = Column(String, nullable=False)
    aadhaar_no = Column(String)
    file = Column(LargeBinary)
    payee_type = Column(String)
    payee_name = Column(String)
    payee_code = Column(String)
    status = Column(String, nullable=False)
    remarks = Column(String)
    email_id = Column(String)
    otp = Column(Integer)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    otp_time = Column(DateTime)
    otp_count = Column(Integer)
    file_type = Column(String)
    undertaking_content = Column(String)
    undertaking_by = Column(String)
    undertaking_date = Column(DateTime)
    undertaking_flag = Column(String, nullable=False)


class AccAccountMaster(Base):
    __tablename__ = 'acc_account_master'

    serial_no = Column(Integer, primary_key=True)
    account_no = Column(String, nullable=False)
    bank_name = Column(String, nullable=False)
    account_description = Column(String)
    opening_balance = Column(Integer)
    closing_balance = Column(Integer)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    for_individual = Column(String)
    ifsc_code = Column(String)
    micr_code = Column(String)
    short_name = Column(String)
    bank_coa = Column(String)
    acc_project_code = Column(String)
    group_acc_type = Column(String)
    inst_vendor_code = Column(String)
    display_flag = Column(String, nullable=False)
    ovh_gst_credited_amt = Column(String)


class AccAdvancedAdjustmentDetails(Base):
    __tablename__ = 'acc_advanced_adjustment_details'

    sl_no = Column(Integer, primary_key=True)
    advanced_bill_no = Column(String)
    payee_id = Column(String)
    chart_of_account_code = Column(Float)
    adjusted_voucher_no = Column(String)
    adjusted_amt = Column(Float)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    project_code = Column(Integer)


class AccAdvancedDetails(Base):
    __tablename__ = 'acc_advanced_details'

    sl_no = Column(Integer, primary_key=True)
    bill_no = Column(String, nullable=False)
    payee_id = Column(String, nullable=False)
    advanced_amt = Column(Float)
    adjusted_amt = Column(Float)
    chart_of_account_code = Column(Float)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    adv_flag = Column(String)
    project_code = Column(Integer)
    adv_block_flag = Column(String, nullable=False)
    adv_blocked_by = Column(String)
    blocked_date = Column(DateTime)


class AccBillNo(Base):
    __tablename__ = 'acc_bill_no'

    bill_predicate = Column(String)
    current_max = Column(Integer)
    transaction_type = Column(String)
    financial_year = Column(String, nullable=False)
    serial_no = Column(Integer, primary_key=True)


class AccBillType(Base):
    __tablename__ = 'acc_bill_type'

    type_no = Column(Integer, primary_key=True)
    type_code = Column(String)
    description = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)


class AccDailyBalance(Base):
    __tablename__ = 'acc_daily_balance'

    acc_no = Column(String, primary_key=True)
    balance_date = Column(Date, nullable=False)
    op_balance = Column(Float)
    receipt_amount = Column(Float)
    payment_amount = Column(Float)
    cl_balance = Column(Float)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modified_date = Column(DateTime)
    deleted_flag = Column(String, nullable=False)
    batch_flag = Column(String)
    batch_run_by = Column(String)
    batch_run_date = Column(DateTime)
    edit_remarks = Column(String)


class AccDailyBalanceBak(Base):
    __tablename__ = 'acc_daily_balance_bak'

    acc_no = Column(String, primary_key=True)
    balance_date = Column(Date)
    op_balance = Column(Float)
    receipt_amount = Column(Float)
    payment_amount = Column(Float)
    cl_balance = Column(Float)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modified_date = Column(DateTime)
    deleted_flag = Column(String)
    batch_flag = Column(String)
    batch_run_by = Column(String)
    batch_run_date = Column(DateTime)
    edit_remarks = Column(String)


class AccountHeadWiseTransaction(Base):
    __tablename__ = 'account_head_wise_transaction'

    financial_year = Column(String, primary_key=True)
    acc_no = Column(String, nullable=False)
    parent_head = Column(Integer, nullable=False)
    child_head = Column(Integer, nullable=False)
    date_of_transaction = Column(Date, nullable=False)
    op_balance = Column(Numeric)
    dr_amt = Column(Numeric)
    cr_amt = Column(Numeric)
    cl_balance = Column(Numeric)
    ref_type = Column(String)
    ref_no = Column(String)
    ref_sl_no = Column(Integer)
    status = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)


class AccountsTransactionHistory(Base):
    __tablename__ = 'accounts_transaction_history'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    process_name = Column(String)
    process_details = Column(String)
    remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)


class AccProjectBalance(Base):
    __tablename__ = 'acc_project_balance'

    project_code = Column(Integer, primary_key=True)
    balance_date = Column(Date, nullable=False)
    op_balance = Column(Float)
    receipt_amount = Column(Float)
    payment_amount = Column(Float)
    cl_balance = Column(Float)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modified_date = Column(DateTime)
    deleted_flag = Column(String, nullable=False)
    edit_remarks = Column(String)


class AccProjectBillReceipt(Base):
    __tablename__ = 'acc_project_bill_receipt'

    receipt_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    payee_code = Column(String)
    project_code = Column(Integer)
    chart_of_account_no = Column(Integer)
    total_amount = Column(Float)
    bill_no = Column(String, nullable=False)
    bill_date = Column(Date)
    bill_type = Column(String)
    file_no = Column(String)
    status = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    head_chart_of_account = Column(Integer)
    pending_to = Column(String, nullable=False)
    office_order_no = Column(String)
    office_order_date = Column(Date)
    hard_copy_received = Column(String)
    reject_flag = Column(String)
    adjusted = Column(String)
    advance_flag = Column(String)
    particular = Column(String)
    advance_receipt_no = Column(Integer)
    pay_flag = Column(String)
    overshoot_remarks = Column(String)
    claim_amt = Column(Float)
    choice1 = Column(String)
    haltat = Column(String)
    choice2 = Column(String)
    choice3 = Column(String)
    choice4 = Column(String)
    fromdate = Column(Date)
    todate = Column(Date)
    boardingplace = Column(String)
    payee_type = Column(String)
    voucher_no = Column(String)
    voucher_date = Column(Date)
    acc_no = Column(String)
    phase = Column(String)
    seq = Column(Integer)
    bill_owner = Column(String)
    owner_type = Column(String)
    rejected_by = Column(String)
    rejection_date = Column(DateTime)
    grant_receipt_no = Column(String)
    ovc_remarks = Column(String)
    st_remarks = Column(String)
    grant_financial_year = Column(String)
    grant_lock_flag = Column(String)
    grant_lock_by = Column(String)
    grant_lock_date = Column(DateTime)
    advance_bill_no = Column(String)
    audit_date = Column(DateTime)
    audit_remarks = Column(String)
    audit_by = Column(String)
    share_flag = Column(String)
    gst_rate = Column(Numeric)
    reverse_charges = Column(String, nullable=False)
    goods_or_service = Column(String, nullable=False)
    base_value = Column(Numeric)
    invoice_no = Column(String)
    invoice_date = Column(DateTime)
    hsn_sac = Column(String)
    gh_demand_no = Column(String)
    is_gem_purchase_flag = Column(String, nullable=False)
    gem_non_availability_cert_no = Column(String)
    non_gem_approving_person = Column(String)
    non_gem_approving_date = Column(Date)
    gem_contract_no = Column(String)
    bill_summarized_lock_flag = Column(String, nullable=False)
    mapping_budget_head = Column(String)


class AccProjectBillReceiptDetails(Base):
    __tablename__ = 'acc_project_bill_receipt_details'

    receipt_details_no = Column(Integer, nullable=False)
    bill_no = Column(String, primary_key=True)
    particulars = Column(String)
    item_no = Column(Integer)
    item_price = Column(Float)
    visit_place = Column(String)
    visit_purpose = Column(String)
    visit_from = Column(Date)
    visit_to = Column(Date)
    amount = Column(Float)
    status_flag = Column(String, nullable=False)
    pending_to = Column(String, nullable=False)
    dep_station = Column(String)
    dep_time = Column(Date)
    arr_station = Column(String)
    arr_time = Column(Date)
    mode_of_journey = Column(String)
    class_of_journey = Column(String)
    no_of_fares_kms = Column(String)
    expenditure = Column(Float)
    ticket_no = Column(String)
    remarks = Column(String)
    ch_dd_no = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    pay_flag = Column(String)
    place_of_visit = Column(String)
    purpose_of_visit = Column(String)
    dfrom = Column(Date)
    dto = Column(Date)
    payment_code = Column(Integer)
    chart_of_account_code = Column(Integer)
    payee_code = Column(String)
    payee_name = Column(String)
    advance_bill_no = Column(String)
    payee_type = Column(String)
    acc_no = Column(String)
    phase = Column(String)
    batch_process = Column(String)
    payee_pay_type = Column(String)
    chalan_no = Column(String)
    chalan_dt = Column(DateTime)
    chalan_payee = Column(String)
    chalan_amt = Column(Numeric)
    chalan_remarks = Column(String)
    chalan_flag = Column(String)
    financial_year = Column(String, nullable=False)


class AccProjectBillReceiptDetailsRaw(Base):
    __tablename__ = 'acc_project_bill_receipt_details_raw'

    receipt_details_no = Column(Integer, nullable=False)
    bill_no = Column(String, primary_key=True)
    particulars = Column(String)
    item_no = Column(Integer)
    item_price = Column(Float)
    visit_place = Column(String)
    visit_purpose = Column(String)
    visit_from = Column(Date)
    visit_to = Column(Date)
    amount = Column(Float)
    status_flag = Column(String, nullable=False)
    pending_to = Column(String, nullable=False)
    dep_station = Column(String)
    dep_time = Column(Date)
    arr_station = Column(String)
    arr_time = Column(Date)
    mode_of_journey = Column(String)
    class_of_journey = Column(String)
    no_of_fares_kms = Column(String)
    expenditure = Column(Float)
    ticket_no = Column(String)
    remarks = Column(String)
    ch_dd_no = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    pay_flag = Column(String)
    place_of_visit = Column(String)
    purpose_of_visit = Column(String)
    dfrom = Column(Date)
    dto = Column(Date)
    payment_code = Column(Integer)
    chart_of_account_code = Column(Integer)
    payee_code = Column(String)
    payee_name = Column(String)
    advance_bill_no = Column(String)
    payee_type = Column(String)
    acc_no = Column(String)
    phase = Column(String)
    sub_vch = Column(String)
    adj_type = Column(String)
    financial_year = Column(String, nullable=False)


class AccProjectPaymentDetails(Base):
    __tablename__ = 'acc_project_payment_details'

    payment_no = Column(Integer, nullable=False)
    financial_year = Column(String, nullable=False)
    project_code = Column(Integer, primary_key=True)
    overhead_details_no = Column(Integer)
    particulars = Column(String)
    ch_dd_no = Column(String)
    servicecharges_overhead_amount = Column(Numeric)
    other_amount = Column(Numeric)
    total_payment_amount = Column(Numeric)
    payment_date = Column(Date)
    amount = Column(Numeric)
    amount_remitted_to_bank = Column(Integer)
    amount_paid_to_others = Column(Integer)
    acc_no = Column(String)
    bill_no = Column(String)
    receipt_details_no = Column(String)
    bill_date = Column(Date)
    voucher_no = Column(String)
    voucher_date = Column(Date)
    file_no = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    opening_balance = Column(Float)
    closing_balance = Column(Float)
    head_chart_of_account = Column(Integer)
    reconciliation = Column(String)
    adjusted_amount = Column(Float)
    remarks = Column(String)
    reconciliation_date = Column(DateTime)
    da_day = Column(Integer)
    da_per_day = Column(Float)
    advance_deduct = Column(Float)
    other_deduction = Column(Float)
    objected_amount = Column(Float)
    reason = Column(String)
    close_path_flag = Column(String)
    tax_code = Column(String)
    pay_flag = Column(String, nullable=False)
    cheque_status = Column(String)
    dispatch_dt = Column(DateTime)
    phase = Column(String)
    pay_type = Column(String)
    chalan_no = Column(String)
    chalan_dt = Column(DateTime)
    chalan_payee = Column(String)
    chalan_amt = Column(Numeric)
    chalan_remarks = Column(String)
    chalan_flag = Column(String)
    rtgs_flag = Column(String)
    gh_pay_flag = Column(String, nullable=False)
    gh_pay_date = Column(DateTime)
    gh_pay_by = Column(String)
    actual_financial_year = Column(String)
    owner_type = Column(String)
    owner_code = Column(String)


class AccProjectPaymentDetailsBkp(Base):
    __tablename__ = 'acc_project_payment_details_bkp'

    payment_no = Column(Integer, nullable=False)
    financial_year = Column(String, nullable=False)
    project_code = Column(Integer, primary_key=True)
    overhead_details_no = Column(Integer)
    particulars = Column(String)
    ch_dd_no = Column(String)
    servicecharges_overhead_amount = Column(Numeric)
    other_amount = Column(Numeric)
    total_payment_amount = Column(Numeric)
    payment_date = Column(Date)
    amount = Column(Numeric)
    amount_remitted_to_bank = Column(Integer)
    amount_paid_to_others = Column(Integer)
    acc_no = Column(String)
    bill_no = Column(String)
    receipt_details_no = Column(String)
    bill_date = Column(Date)
    voucher_no = Column(String)
    voucher_date = Column(Date)
    file_no = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    opening_balance = Column(Float)
    closing_balance = Column(Float)
    head_chart_of_account = Column(Integer)
    reconciliation = Column(String)
    adjusted_amount = Column(Float)
    remarks = Column(String)
    reconciliation_date = Column(DateTime)
    da_day = Column(Integer)
    da_per_day = Column(Float)
    advance_deduct = Column(Float)
    other_deduction = Column(Float)
    objected_amount = Column(Float)
    reason = Column(String)
    close_path_flag = Column(String)
    tax_code = Column(String)
    pay_flag = Column(String, nullable=False)
    cheque_status = Column(String)
    dispatch_dt = Column(DateTime)
    phase = Column(String)
    pay_type = Column(String)
    chalan_no = Column(String)
    chalan_dt = Column(DateTime)
    chalan_payee = Column(String)
    chalan_amt = Column(Numeric)
    chalan_remarks = Column(String)
    chalan_flag = Column(String)
    rtgs_flag = Column(String)


class AccProjectReceiptDetails(Base):
    __tablename__ = 'acc_project_receipt_details'

    receipt_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    project_code = Column(Integer)
    overhead_details_no = Column(Integer)
    ch_dd_no = Column(String)
    receipt_amount = Column(Numeric)
    receipt_date = Column(Date)
    amount_creditable_to_bank = Column(Float)
    amount_due_to_others = Column(Float)
    acc_no = Column(String)
    expected_return_date = Column(Date)
    loan_project_code = Column(Integer)
    voucher_no = Column(String)
    voucher_date = Column(Date)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    opening_balance = Column(Float)
    closing_balance = Column(Float)
    head_chart_of_account = Column(Integer)
    receipt_from = Column(Integer)
    reconciliation = Column(String)
    adjusted_amount = Column(Float)
    remarks = Column(String)
    reconciliation_date = Column(Date)
    service_charge_bill_no = Column(String)
    refund_against_bill_no = Column(String)
    loan_payment_bill_no = Column(String)
    loan_refund_flag = Column(String)
    loan_refund_date = Column(Date)
    individual_code = Column(String)
    bank_credit_date = Column(Date)
    receipt_status = Column(String)
    receipt_remarks = Column(String)
    credited_by = Column(String)
    credited_date = Column(Date)
    receipt_mode = Column(String)
    drawn_on = Column(String)
    in_favour_of = Column(String)
    sponsor_letter_no = Column(String)
    receipt_order_no = Column(String)
    receipt_order_dt = Column(Date)
    ovc_remarks = Column(String)
    st_remarks = Column(String)
    fund_dist_flag = Column(String)
    grant_lock_flag = Column(String)
    grant_lock_by = Column(String)
    grant_lock_date = Column(DateTime)
    currency_type = Column(String)
    currency_desc = Column(String)
    scheem_type = Column(String)
    hsn_sac = Column(String)
    gst_rate = Column(Numeric)
    reverse_charges = Column(String, nullable=False)
    goods_or_service = Column(String, nullable=False)
    base_value = Column(Numeric)
    igst_bill_no = Column(String)
    cgst_bill_no = Column(String)
    sgst_bill_no = Column(String)
    invoice_no = Column(String)
    invoice_date = Column(DateTime)
    gst_bill_no = Column(String)
    invoice_value = Column(Numeric)
    cgst = Column(Numeric)
    sgst = Column(Numeric)
    igst = Column(Numeric)
    tds = Column(Numeric)
    tds_cgst = Column(Numeric)
    tds_sgst = Column(Numeric)
    tds_igst = Column(Numeric)
    other_deduction = Column(Numeric)
    other_deduction_remarks = Column(String)
    actual_financial_year = Column(String)
    email_sent_date = Column(DateTime)
    grant_dist_remarks = Column(String)
    owner_type = Column(String)
    owner_code = Column(String)


class AccProjectReceiptPaymentDeclaration(Base):
    __tablename__ = 'acc_project_receipt_payment_declaration'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    sponsor_code = Column(Integer, nullable=False)
    ref_inv_no = Column(String)
    gross_amount = Column(Numeric)
    net_amount = Column(Numeric)
    tds = Column(Numeric)
    tds_gst = Column(Numeric)
    with_hold_amount = Column(Numeric)
    utr_no = Column(String)
    date_of_transaction = Column(Date)
    destination_acc_no = Column(String)
    reason_for_deduction = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    financial_year = Column(String)
    remarks = Column(String)
    status = Column(String, nullable=False)
    file = Column(LargeBinary)
    rp_id = Column(String)
    receipt_voucher_no = Column(String)
    voucher_date = Column(Date)
    sric_cancel_remarks = Column(String)


class AccTaxDetails(Base):
    __tablename__ = 'acc_tax_details'

    serial_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    bill_no = Column(String)
    tax_code = Column(Integer)
    amount = Column(Float)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    bill_amount = Column(Float)
    ch_no = Column(String)
    ch_dt = Column(Date)
    chalan_no = Column(String)
    chalan_dt = Column(Date)
    payee_code = Column(String)
    payee_type = Column(String)


class AccTaxMaster(Base):
    __tablename__ = 'acc_tax_master'

    serial_no = Column(Integer, primary_key=True)
    tax_code = Column(Integer)
    percent = Column(Float)
    from_date = Column(Date)
    to_date = Column(Date)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    of = Column(Integer)
    tax_type = Column(String)


class AccTaxNameMaster(Base):
    __tablename__ = 'acc_tax_name_master'

    serial_no = Column(Integer, primary_key=True)
    tax_description = Column(String)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)


class AccVchNo(Base):
    __tablename__ = 'acc_vch_no'

    vch_predicate = Column(String)
    current_max = Column(Integer)
    serial_no = Column(Integer, primary_key=True)


class AccVoucherType(Base):
    __tablename__ = 'acc_voucher_type'

    serial_no = Column(Integer, primary_key=True)
    voucher_code = Column(String)
    description = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)


class AdmStakeHolderRoleDetail(Base):
    __tablename__ = 'adm_stake_holder_role_detail'

    stake_holder_code = Column(Integer, primary_key=True)
    role_code = Column(String)


class Anitax(Base):
    __tablename__ = 'anitax'

    empno = Column(String, primary_key=True)
    empname = Column(String)
    empdesg = Column(String)
    empdept = Column(String)
    salcode = Column(String)
    salsrno = Column(String)
    sex = Column(String)
    pan_gir_no = Column(String)
    basic = Column(Numeric, nullable=False)
    da = Column(Numeric, nullable=False)
    arrda = Column(Numeric, nullable=False)
    ir = Column(Numeric, nullable=False)
    arrir = Column(Numeric, nullable=False)
    splpay = Column(Numeric, nullable=False)
    miscpay = Column(Numeric, nullable=False)
    odhra = Column(Numeric, nullable=False)
    hpl = Column(Numeric, nullable=False)
    hra = Column(Numeric, nullable=False)
    hra_exempt = Column(Numeric, nullable=False)
    unfurnished = Column(Numeric, nullable=False)
    furnished = Column(Numeric, nullable=False)
    tot_sal_income = Column(Numeric, nullable=False)
    std_ded = Column(Numeric, nullable=False)
    ptax = Column(Numeric, nullable=False)
    hba = Column(Numeric, nullable=False)
    charge_income = Column(Numeric, nullable=False)
    jee_honr = Column(Numeric, nullable=False)
    gate_honor = Column(Numeric, nullable=False)
    consul_honor = Column(Numeric, nullable=False)
    interest_nsc = Column(Numeric, nullable=False)
    other_honor = Column(Numeric, nullable=False)
    tot_oth_income = Column(Numeric, nullable=False)
    gross = Column(Numeric, nullable=False)
    ded_5_1 = Column(Numeric, nullable=False)
    ded_5_2 = Column(Numeric, nullable=False)
    ded_5_3 = Column(Numeric, nullable=False)
    ded_5_4 = Column(Numeric, nullable=False)
    ded_5_5 = Column(Numeric, nullable=False)
    ded_5_6 = Column(Numeric, nullable=False)
    ded_5_7 = Column(Numeric, nullable=False)
    tot_5_8 = Column(Numeric, nullable=False)
    income_6_a = Column(Numeric, nullable=False)
    income_6_b = Column(Numeric, nullable=False)
    itax_7 = Column(Numeric, nullable=False)
    rebate_8_1 = Column(Numeric, nullable=False)
    rebate_8_2 = Column(Numeric, nullable=False)
    rebate_8_3 = Column(Numeric, nullable=False)
    rebate_8_4 = Column(Numeric, nullable=False)
    rebate_8_5 = Column(Numeric, nullable=False)
    rebate_8_6 = Column(Numeric, nullable=False)
    rebate_8_7 = Column(Numeric, nullable=False)
    rebate_8_8 = Column(Numeric, nullable=False)
    rebate_8_9 = Column(Numeric, nullable=False)
    rebate_8_10 = Column(Numeric, nullable=False)
    rebate_8_11 = Column(Numeric, nullable=False)
    rebate_8_12 = Column(Numeric, nullable=False)
    rebate_8_13 = Column(Numeric, nullable=False)
    tax_rebate_16 = Column(Numeric, nullable=False)
    rebate_9 = Column(Numeric, nullable=False)
    rebate_9_2 = Column(Numeric, nullable=False)
    relief_10_2 = Column(Numeric, nullable=False)
    itax_11_1 = Column(Numeric, nullable=False)
    tax_ded_source = Column(Numeric, nullable=False)
    tax_ded_salary = Column(Numeric, nullable=False)
    tax_ded_cash = Column(Numeric, nullable=False)
    tax_ded_jee = Column(Numeric, nullable=False)
    tax_ded_gate = Column(Numeric, nullable=False)
    tax_ded_con = Column(Numeric, nullable=False)
    tax_ded_oth = Column(Numeric, nullable=False)
    balance_itax = Column(Numeric, nullable=False)
    royalty = Column(Numeric, nullable=False)
    sup_bill = Column(Numeric, nullable=False)
    ded_5_6_2 = Column(Numeric, nullable=False)
    fpc_arr = Column(Numeric, nullable=False)
    itax_refund = Column(Numeric, nullable=False)
    flag1 = Column(String)
    tax_capgain = Column(Numeric, nullable=False)
    ded_5_8 = Column(Numeric, nullable=False)
    rebate_female = Column(Numeric, nullable=False)
    surcharge = Column(Numeric, nullable=False)
    net_payable = Column(Numeric, nullable=False)
    rebate_8_qualify = Column(Numeric, nullable=False)
    rebate_9_1 = Column(Numeric, nullable=False)
    tax_payable_88 = Column(Numeric, nullable=False)
    foreign_remu = Column(Numeric, nullable=False)
    family_pension = Column(Numeric, nullable=False)
    ded_5_9 = Column(Numeric, nullable=False)
    rebate_88d = Column(Numeric, nullable=False)
    cess = Column(Numeric, nullable=False)
    ded_5_10 = Column(Numeric, nullable=False)
    flag2 = Column(String)
    std_ded_1 = Column(Numeric)
    std_ded_2 = Column(Numeric)
    finyear = Column(String, nullable=False)
    emp_type = Column(String, nullable=False)


class ApplyForExpCertificate(Base):
    __tablename__ = 'apply_for_exp_certificate'

    sl_no = Column(Integer, primary_key=True)
    sric_id = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    pi_guide = Column(String, nullable=False)
    desg_id = Column(String, nullable=False)
    from_date = Column(Date, nullable=False)
    exp_to_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    cert_id = Column(String)
    cert_generation_date = Column(DateTime)
    cert_generated_by = Column(String)
    creation_date = Column(DateTime)
    remarks = Column(String)
    project_status = Column(String, nullable=False)
    request_date = Column(Date, nullable=False)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    file_path = Column(String)
    order_number = Column(String)
    justification = Column(String)
    just_file_id = Column(String)
    working_status = Column(String, nullable=False)
    certificate_from_date = Column(Date)
    certificate_to_date = Column(Date)


class AssignmentDetails(Base):
    __tablename__ = 'assignment_details'

    serial_no = Column(Integer, primary_key=True)
    assignor_id = Column(String)
    role_code = Column(String)
    assignee_id = Column(String)
    assignment_type = Column(String)
    assignments = Column(String)
    course_code = Column(String)
    course_year = Column(String)
    lab_code = Column(String)
    acad_session = Column(String)
    acad_semester = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    remarks = Column(String)
    completion_status = Column(Boolean)
    completion_date = Column(Date)
    co_incharge = Column(String)
    unstructured_work = Column(String)
    delete_flag = Column(Boolean)
    preparator_id = Column(String)
    to_be_corrected = Column(Boolean)
    confirmation_flag = Column(Boolean)
    corrections = Column(String)
    dept_code = Column(String)


class AssignTaDaAccess(Base):
    __tablename__ = 'assign_ta_da_access'

    assignee_id = Column(String, nullable=False)
    role_code = Column(String, nullable=False)
    project_code = Column(String, primary_key=True)
    sl_no = Column(Integer, nullable=False)
    from_dt = Column(Date)
    to_dt = Column(Date)
    appv_id = Column(String)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)


class AttachmentMaster(Base):
    __tablename__ = 'attachment_master'

    attachment_code = Column(String, primary_key=True)
    attachment_desc = Column(String)


class BalanceSheet(Base):
    __tablename__ = 'balance_sheet'

    fin_year = Column(String, primary_key=True)
    org_id = Column(String, nullable=False)
    project_id = Column(String, nullable=False)
    head_id = Column(Integer, nullable=False)
    acc_no = Column(String, nullable=False)
    op_bal = Column(Numeric)
    dr_amt = Column(Numeric)
    cr_amt = Column(Numeric)
    cl_bal = Column(Numeric)
    status = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    sl_no = Column(Integer, nullable=False)


class BankRgtsRate(Base):
    __tablename__ = 'bank_rgts_rate'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    ifsc = Column(String)
    bank_name = Column(String)
    bank_address = Column(String)
    delete_flag = Column(String)
    charges = Column(Float)
    micr = Column(String)
    from_amount = Column(Float)
    to_amount = Column(Float)


class BankRtgs(Base):
    __tablename__ = 'bank_rtgs'

    bill_no = Column(String, primary_key=True)
    payee_code = Column(String, nullable=False)
    net_amount = Column(Float)
    bank_charges = Column(Float)
    save_flag = Column(String)
    delete_flag = Column(String)
    lock_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime, nullable=False)
    modification_by = Column(String)
    modification_date = Column(DateTime)
    remarks = Column(String)
    acc_no = Column(String)
    cheque_no = Column(String)


class BillDiaryEntry(Base):
    __tablename__ = 'bill_diary_entry'

    sl_no = Column(Integer, primary_key=True)
    fin_yr = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    scheme_code = Column(String)
    component_code = Column(String)
    chart_of_account_code = Column(Integer)
    payee_type = Column(String)
    payee_code = Column(String, nullable=False)
    remarks = Column(String)
    amount = Column(Numeric)
    status = Column(String, nullable=False)
    ta_ref_no = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    diary_no = Column(String, nullable=False)
    verified_amount = Column(Numeric)
    appv_no = Column(String)
    purchase_no = Column(String)
    temp_user_code = Column(String)


class BillDiaryEntryHistory(Base):
    __tablename__ = 'bill_diary_entry_history'

    sl_no = Column(Integer, primary_key=True)
    diary_no = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    scheme_code = Column(String)
    component_code = Column(String)
    chart_of_account_code = Column(Integer)
    payee_type = Column(String)
    payee_code = Column(String, nullable=False)
    remarks = Column(String)
    amount = Column(Numeric)
    status = Column(String, nullable=False)
    ta_ref_no = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    fin_yr = Column(String, nullable=False)


class BillOfSupply(Base):
    __tablename__ = 'bill_of_supply'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    org_id = Column(String, nullable=False)
    project_id = Column(Integer, nullable=False)
    invoice_date = Column(Date, nullable=False)
    invoice_no = Column(String, nullable=False)
    supplier_id = Column(String)
    hsn_sac = Column(String)
    bill_amount = Column(Numeric)
    customer_id = Column(String)
    customer_name = Column(String)
    consignee_id = Column(String)
    consignee_name = Column(String)
    supply_date = Column(DateTime)
    supply_state = Column(String)
    goods_or_service = Column(String)
    status = Column(String)
    remarks = Column(String)
    actual_invoice_id = Column(String)
    bos_mst_com_pk = Column(String)
    reference_id = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    reverse_charges = Column(String, nullable=False)
    uom = Column(String)
    qty = Column(Integer)
    description = Column(String)
    bos_year = Column(String)


class BudgetAllocation(Base):
    __tablename__ = 'budget_allocation'

    project_code = Column(Integer, primary_key=True)
    phase = Column(Integer, nullable=False)
    parent_account_code = Column(Integer, nullable=False)
    account_code = Column(Integer, nullable=False)
    budgetted_amount = Column(Float)
    actual_expense_amount = Column(Float)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    booked_amount = Column(Float)


class BudgetAllocationMaster(Base):
    __tablename__ = 'budget_allocation_master'

    project_code = Column(Integer, primary_key=True)
    phase = Column(Integer, nullable=False)
    total_budgetted_amount = Column(Float)
    total_expense_amount = Column(Float)
    utilization_flag = Column(String)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    from_date = Column(Date)
    to_date = Column(Date)
    allow_sc_flag = Column(String)
    remarks = Column(String)


class BudgetHeadMappingToOthersHead(Base):
    __tablename__ = 'budget_head_mapping_to_others_head'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    parent_acc_head = Column(Integer, nullable=False)
    account_head = Column(Integer, nullable=False)
    mapping_budget_head = Column(Integer)
    mapping_p_head = Column(Integer)
    mapping_upto = Column(Date)
    justification = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    modified_by = Column(String)
    modification_date = Column(Date)


class BudgetMappingInExpenditureHead(Base):
    __tablename__ = 'budget_mapping_in_expenditure_head'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    phase = Column(Integer, nullable=False)
    parent_acc_head = Column(Integer, nullable=False)
    account_head = Column(Integer, nullable=False)
    mapping_budget_head = Column(Integer)
    amount = Column(Numeric)
    created_by = Column(String)
    creation_date = Column(DateTime)
    mapping_p_head = Column(Integer)


class BudgetMappingWithExpenditureHead(Base):
    __tablename__ = 'budget_mapping_with_expenditure_head'

    project_code = Column(Integer, primary_key=True)
    expenditure_head = Column(Integer, nullable=False)
    budget_head = Column(Integer, nullable=False)
    delete_flag = Column(String)
    created_by = Column(String)
    created_ts = Column(DateTime)


class Category(Base):
    __tablename__ = 'category'

    cat_code = Column(String, primary_key=True)
    cat_name = Column(String)


class ChartOfAccounts(Base):
    __tablename__ = 'chart_of_accounts'

    account_code = Column(Integer, primary_key=True)
    account_description = Column(String)
    account_type = Column(String)
    account_level = Column(Integer)
    parent_account_code = Column(Integer)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    type = Column(String)
    tax_section = Column(String)
    challan_flg = Column(String)
    adj_mapping_head = Column(Integer)
    tax_rate = Column(Numeric)
    acc_head_mapping = Column(String)
    display_flag = Column(String, nullable=False)
    hono_group_head = Column(String)
    budget_flag = Column(String, nullable=False)
    balance_sheet_adv_adj_mapping_head = Column(String)
    allow_sc_flag = Column(String, nullable=False)
    allow_common_exp_flag = Column(String)
    display_serb_budget_head_desc_for_uc = Column(String)
    display_serb_budget_order_by_for_uc = Column(Integer)
    broad_head_clasification = Column(String)


class ChkDispatchDetails(Base):
    __tablename__ = 'chk_dispatch_details'

    sl_no = Column(Integer, primary_key=True)
    cheque_no = Column(String, nullable=False)
    cheque_dt = Column(Date, nullable=False)
    acc_no = Column(String, nullable=False)
    payee_name = Column(String)
    cheque_type = Column(String)
    amount = Column(Numeric)
    vch_no = Column(String)
    vch_dt = Column(Date)
    dispatch_dt = Column(DateTime)
    pay_reconciliation_dt = Column(Date)
    remarks = Column(String)
    dispatch_remarks = Column(String)
    reconciliation_remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modification_by = Column(String)
    modification_date = Column(DateTime)
    print_flag = Column(String)
    reconciliation_flag = Column(String)
    dispatch_flag = Column(String)
    delete_flag = Column(String)
    bill_no = Column(String)
    project_code = Column(String)
    user_project_code = Column(String)
    print_dt = Column(DateTime)
    status = Column(String)
    receipt_details_no = Column(Integer)
    payment_no = Column(Integer)
    unlock_remarks = Column(String)
    unlock_by = Column(String)
    unlock_dt = Column(DateTime)
    unlock_flag = Column(String)
    pay_type = Column(String)
    consol_amt = Column(String)
    file_name = Column(String)
    file_path = Column(String)
    dispatch_by = Column(String)
    financial_year = Column(String)
    send_mail_flag = Column(String)
    no_of_send_mail = Column(Integer)
    send_by = Column(String)
    send_date = Column(DateTime)
    cheque_status = Column(String)
    status_remarks = Column(String)


class ChkDispatchDetailsHistory(Base):
    __tablename__ = 'chk_dispatch_details_history'

    sl_no = Column(Integer, primary_key=True)
    cheque_no = Column(String, nullable=False)
    cheque_dt = Column(Date, nullable=False)
    acc_no = Column(String, nullable=False)
    payee_name = Column(String)
    cheque_type = Column(String)
    amount = Column(Numeric)
    vch_no = Column(String)
    vch_dt = Column(Date)
    dispatch_dt = Column(DateTime)
    pay_reconciliation_dt = Column(Date)
    remarks = Column(String)
    dispatch_remarks = Column(String)
    reconciliation_remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modification_by = Column(String)
    modification_date = Column(DateTime)
    print_flag = Column(String)
    reconciliation_flag = Column(String)
    dispatch_flag = Column(String)
    delete_flag = Column(String)
    bill_no = Column(String)
    project_code = Column(String)
    user_project_code = Column(String)
    print_dt = Column(DateTime)
    status = Column(String)
    receipt_details_no = Column(Integer)
    payment_no = Column(Integer)
    unlock_remarks = Column(String)
    unlock_by = Column(String)
    unlock_dt = Column(DateTime)
    unlock_flag = Column(String)
    pay_type = Column(String)
    consol_amt = Column(String)
    financial_year = Column(String)
    cheque_status = Column(String)
    status_remarks = Column(String)


class ClaimForFellowship(Base):
    __tablename__ = 'claim_for_fellowship'

    sl_no = Column(Integer, primary_key=True)
    empno = Column(String, nullable=False)
    yr = Column(String, nullable=False)
    mon = Column(String, nullable=False)
    acc_no = Column(String)
    file_path = Column(String)
    project_code = Column(String, nullable=False)
    claim_amount = Column(Numeric)
    net_amount = Column(Numeric)
    pending_to = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    bill_no = Column(String)
    claim_id = Column(String)


class ClaimForTaDa(Base):
    __tablename__ = 'claim_for_ta_da'

    appv_no = Column(String, nullable=False)
    financial_year = Column(String, nullable=False)
    dep_station = Column(String)
    dep_date = Column(Date)
    dep_hh = Column(String)
    dep_mm = Column(String)
    arr_station = Column(String)
    arr_date = Column(Date)
    arr_hh = Column(String)
    arr_mm = Column(String)
    mode_of_journey = Column(String)
    class_of_journey = Column(String)
    no_of_fares = Column(String)
    toll_tax = Column(String)
    parking_charge = Column(String)
    particular = Column(String)
    amount = Column(String)
    reimburse_type = Column(String)
    reimburse_by = Column(String)
    kms = Column(String)
    sricvrfy = Column(String)
    sricremarks = Column(String)
    auditvrfy = Column(String)
    auditremarks = Column(String)
    claim_type = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modification_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String)
    workflow_id = Column(String)
    instance_id = Column(Integer)
    ta_amount = Column(String)
    reim_remarks = Column(String)
    workflow_status = Column(String)
    choice1 = Column(String)
    choice2 = Column(String)
    choice3 = Column(String)
    choice4 = Column(String)
    choice5 = Column(String)
    advance_bill_no = Column(String)
    from_dt = Column(Date)
    to_date = Column(Date)
    boarding_place = Column(String)
    sl_no = Column(Integer, primary_key=True)
    purpose_of_journey = Column(String)
    payee_type = Column(String)
    payee_code = Column(String, nullable=False)
    project_code = Column(Integer)
    advance_amount = Column(String)
    advance_bill_date = Column(Date)
    applicant_remarks = Column(String)


class ComBankDetails(Base):
    __tablename__ = 'com_bank_details'

    stake_holder_code = Column(Text, primary_key=True)
    adhaar_bank_acc_no = Column(Text)
    adhaar_bank_branch_name = Column(Text)
    adhaar_bank_ifsc_code = Column(Text)
    adhaar_bank_name = Column(Text)
    bank_acc_no = Column(Text)
    bank_ifsc_code = Column(Text)


class ConsultancyOverheadDetails(Base):
    __tablename__ = 'consultancy_overhead_details'

    serial_no = Column(Integer, primary_key=True)
    description = Column(String)
    percent = Column(Float)
    office_order_no = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    overhead_code = Column(Float)
    project_type = Column(String)
    ovh_type = Column(String)
    bog_appv = Column(String, nullable=False)
    ovh_type_desc = Column(String)


class CrfExternalAppDetails(Base):
    __tablename__ = 'crf_external_app_details'

    financial_year = Column(String, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    account_no = Column(Numeric, nullable=False)
    demand_no = Column(String)
    customer_name = Column(String, nullable=False)
    customer_address = Column(String)
    gstin = Column(String)
    pan = Column(String)
    state = Column(String)
    country = Column(String)
    contact_no = Column(String)
    email_id = Column(String, nullable=False)
    transaction_no = Column(String)
    transaction_date = Column(Date)
    equip_id = Column(String, nullable=False)
    equip_amount = Column(Numeric)
    remarks = Column(String)
    cust_bank_name = Column(String)
    cust_bank_acc_no = Column(String)
    cust_bank_address = Column(String)
    ifsc_code = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    inv_no = Column(String)
    inv_generation_date = Column(DateTime)
    inv_flag = Column(String, nullable=False)
    receipt_no = Column(Integer)
    receipt_date = Column(DateTime)
    receipt_financial_year = Column(String)
    status = Column(String, nullable=False)
    application_id = Column(String, nullable=False)
    org_type = Column(String)
    no_of_samples = Column(Integer)
    sample_description = Column(String)
    analysis_required = Column(String)
    pincode = Column(Integer)
    proforma_inv_no = Column(String)
    invoice_no = Column(String)
    cust_ref_no = Column(String)


class DaDetails(Base):
    __tablename__ = 'da_details'

    org_id = Column(String, primary_key=True)
    payee_id = Column(String, nullable=False)
    slno = Column(Integer, nullable=False)
    sub_slno = Column(Integer, nullable=False)
    from_date = Column(DateTime)
    form_time = Column(String)
    to_date = Column(DateTime)
    to_time = Column(String)
    no_of_days = Column(Numeric)
    rate = Column(Numeric)
    claimed_amount = Column(Numeric)
    verified_amount = Column(Numeric)
    verification_flag = Column(String)
    place = Column(String)
    remarks = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    currency_type = Column(String)
    da_type = Column(String)
    diary_no = Column(String, nullable=False)


class DdfBalance(Base):
    __tablename__ = 'ddf_balance'

    financial_year = Column(String, nullable=False)
    research_dept_code = Column(String, nullable=False)
    ddf_op_balance = Column(Numeric)
    ddf_receipt_amount = Column(Numeric)
    ddf_payment_amount = Column(Numeric)
    ddf_cl_balance = Column(Numeric)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String)
    sl_no = Column(Integer, primary_key=True)
    ref_no = Column(Integer)
    ref_type = Column(String)
    ref_financial_yr = Column(String)
    remarks = Column(String)
    chart_of_account = Column(String)
    edit_remarks = Column(String)
    balance_date = Column(Date)


class DdfDetails(Base):
    __tablename__ = 'ddf_details'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    receipt_no = Column(Integer)
    project_code = Column(Integer, nullable=False)
    dept = Column(String, nullable=False)
    overhead_receipt_amount = Column(Numeric)
    ddf_share_amount = Column(Numeric)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    overhead_amount = Column(Numeric)
    lock_flag = Column(String, nullable=False)
    demand_no = Column(String)
    phase = Column(Integer, nullable=False)


class DdfFdfMaster(Base):
    __tablename__ = 'ddf_fdf_master'

    financial_year = Column(String, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    receipt_no = Column(Integer)
    project_code = Column(Integer, nullable=False)
    project_type = Column(String)
    overhead_receipt_amount = Column(Numeric)
    ddf_share_amount = Column(Numeric)
    fdf_share_amount = Column(Numeric)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    overhead_amount = Column(Numeric)
    lock_flag = Column(String, nullable=False)
    phase = Column(Integer, nullable=False)


class DemandEntry(Base):
    __tablename__ = 'demand_entry'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    acc_no = Column(String, nullable=False)
    chart_of_account_no = Column(Integer, nullable=False)
    ref_id = Column(String, nullable=False)
    demand_no = Column(String, nullable=False)
    demand_type = Column(String, nullable=False)
    demand_date = Column(Date)
    remarks = Column(String)
    amount = Column(Numeric)
    status = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    inst_vendor_code = Column(String)
    ddf_code = Column(String)
    fdf_code = Column(String)


class DeptRoleMaster(Base):
    __tablename__ = 'dept_role_master'

    role_code = Column(String, primary_key=True)
    role_type = Column(String)
    role_description = Column(String)
    local = Column(String)
    parent_role_code = Column(String)
    active_flag = Column(String)


class DesignationSpecialization(Base):
    __tablename__ = 'designation_specialization'

    sl_no = Column(Integer, primary_key=True)
    specialization_desc = Column(String)
    remarks = Column(String)
    delete_flag = Column(String, nullable=False)
    creation_date = Column(DateTime)
    created_by = Column(String)
    modified_by = Column(String)
    modification_date = Column(DateTime)


class Doctemplate(Base):
    __tablename__ = 'doctemplate'

    doc_temp_id = Column(String, primary_key=True)
    version_no = Column(String, nullable=False)
    block_no = Column(Integer, nullable=False)
    content = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)


class Dpcode(Base):
    __tablename__ = 'dpcode'

    dept = Column(String, primary_key=True)
    depname = Column(String)
    deptype = Column(String)
    depsubtype = Column(String)
    type_order = Column(String)


class DynamicBankAccVendor(Base):
    __tablename__ = 'dynamic_bank_acc_vendor'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(String, nullable=False)
    financial_year = Column(String, nullable=False)
    amount = Column(String, nullable=False)
    payee_name = Column(String, nullable=False)
    payee_address = Column(String, nullable=False)
    payee_state = Column(String, nullable=False)
    payee_country = Column(String, nullable=False)
    payee_pincode = Column(String, nullable=False)
    bank_acc_no1 = Column(String, nullable=False)
    bank_acc_no2 = Column(String, nullable=False)
    bank_name = Column(String)
    bank_ifsc = Column(String)
    micr = Column(String)
    gstin = Column(String)
    panno = Column(String)
    account_head = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    created_ts = Column(DateTime)
    modified_by = Column(String)
    modified_ts = Column(DateTime)
    status = Column(String, nullable=False)
    ref_no = Column(String)
    doc_id = Column(String)
    remarks = Column(String)
    recovary_amount = Column(String)
    recovary_head = Column(String)
    other_recovary_amount = Column(String)
    other_recovary_head = Column(String)
    eoffice_appv_no = Column(String)
    eoffice_appv_date = Column(DateTime)
    payee_id = Column(String, nullable=False)
    fdf_ddf = Column(String)


class ElectronicGstLedger(Base):
    __tablename__ = 'electronic_gst_ledger'

    org_id = Column(String, nullable=False)
    project_id = Column(String, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    from_date = Column(Date)
    gst_to_date = Column(Date)
    igst_payable = Column(Numeric)
    cgst_payable = Column(Numeric)
    sgst_payable = Column(Numeric)
    igst_itc = Column(Numeric)
    cgst_itc = Column(Numeric)
    sgst_itc = Column(Numeric)
    diff_igst = Column(Numeric)
    diff_cgst = Column(Numeric)
    diff_sgst = Column(Numeric)
    e_ledger_op_bal = Column(Numeric)
    e_ledger_receipt = Column(Numeric)
    e_ledger_payment = Column(Numeric)
    e_ledger_cl_bal = Column(Numeric)
    date_of_payment = Column(Date)
    ref_id = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)


class EmpAccountDetails(Base):
    __tablename__ = 'emp_account_details'

    sl_no = Column(Integer, primary_key=True)
    stakeholder_code = Column(String, nullable=False)
    stakeholder_type = Column(String)
    dept = Column(String)
    account_no = Column(String)
    delete_flag = Column(String)
    bank_name = Column(String)
    bank_address = Column(String)
    ifsc = Column(String)
    micr = Column(String)
    remaks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    pan_no = Column(String)
    lock_flag = Column(String)


class EmpAccountDetailsHistory(Base):
    __tablename__ = 'emp_account_details_history'

    sl_no = Column(Integer, primary_key=True)
    stakeholder_code = Column(String, nullable=False)
    stakeholder_type = Column(String, nullable=False)
    dept = Column(String)
    account_no = Column(String)
    delete_flag = Column(String)
    bank_name = Column(String)
    bank_address = Column(String)
    ifsc = Column(String)
    micr = Column(String)
    remaks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    pan_no = Column(String)
    lock_flag = Column(String)


class EmpdesgMaster(Base):
    __tablename__ = 'empdesg_master'

    designation_code = Column(String, primary_key=True)
    designation_desc = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    req_qualification = Column(String)
    adv_flag = Column(String)
    desired_experience = Column(String)
    remarks = Column(String)
    salary_fellowship_from = Column(Float)
    salary_fellowship_to = Column(Float)


class EmptypeMaster(Base):
    __tablename__ = 'emptype_master'

    emptype_code = Column(String, primary_key=True)
    emptype_desc = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)


class ErpAdmMenu(Base):
    __tablename__ = 'erp_adm_menu'

    menu_id = Column(Numeric, primary_key=True)
    display_name = Column(String)
    parent_menu_id = Column(Numeric)
    link = Column(String)
    module_id = Column(Numeric)
    menu_desc = Column(String)
    delete_flag = Column(String)
    can_be_delegated = Column(String)
    crud_c_enabled = Column(String)
    crud_r_enabled = Column(String)
    crud_u_enabled = Column(String)
    crud_d_enabled = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    with_credential = Column(String)
    user_manual = Column(String)
    process_description = Column(String)


class ErpAdmMenuSublinks(Base):
    __tablename__ = 'erp_adm_menu_sublinks'

    menu_id = Column(Numeric, primary_key=True)
    slno = Column(Integer, nullable=False)
    sublink = Column(String)


class FdfBalance(Base):
    __tablename__ = 'fdf_balance'

    financial_year = Column(String, nullable=False)
    empno = Column(String, nullable=False)
    fdf_op_balance = Column(Numeric)
    fdf_receipt_amount = Column(Numeric)
    fdf_payment_amount = Column(Numeric)
    fdf_cl_balance = Column(Numeric)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    sl_no = Column(Integer, primary_key=True)
    ref_no = Column(Integer)
    ref_type = Column(String)
    ref_financial_yr = Column(String)
    remarks = Column(String)
    chart_of_account = Column(String)
    pan_no = Column(String)
    edit_remarks = Column(String)
    balance_date = Column(Date)


class FdfDetails(Base):
    __tablename__ = 'fdf_details'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    receipt_no = Column(Integer)
    project_code = Column(Integer, nullable=False)
    empno = Column(String, nullable=False)
    overhead_receipt_amount = Column(Numeric)
    fdf_share_amount = Column(Numeric)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    overhead_amount = Column(Numeric)
    lock_flag = Column(String, nullable=False)
    demand_no = Column(String)
    phase = Column(Integer, nullable=False)


class FdfTest(Base):
    __tablename__ = 'fdf_test'

    sl_no = Column(String, primary_key=True)
    empno = Column(String, nullable=False)
    cl_balance = Column(String)
    type_1 = Column(String)


class FeeLedger(Base):
    __tablename__ = 'fee_ledger'

    rollno = Column(String, primary_key=True)
    session = Column(String)
    semester = Column(String)
    mess_fee = Column(String)
    hall = Column(String)
    date_of_payment = Column(DateTime)
    physical_ver = Column(String)
    amount_paid = Column(String)
    mode_of_payment = Column(String)
    remarks = Column(String)


class FinalAccBasicData(Base):
    __tablename__ = 'final_acc_basic_data'

    org_id = Column(String, primary_key=True)
    fy_date = Column(Date, nullable=False)
    slno = Column(Integer, nullable=False)
    financial_year = Column(String)
    cost_center_id = Column(String)
    project_id = Column(String)
    head_id = Column(Integer)
    dr_amt = Column(Numeric)
    cr_amt = Column(Numeric)
    ref_no = Column(String)
    acc_no = Column(String)
    project_type = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    account_type = Column(String)
    transaction_type = Column(String)
    ref_sl_no = Column(String)
    ref_financial_year = Column(String)
    status = Column(String)


class FinancialTransactionLockUnlockHistory(Base):
    __tablename__ = 'financial_transaction_lock_unlock_history'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    transaction_type = Column(String, nullable=False)
    status = Column(String)
    working_date = Column(Date)
    remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)


class FinancialYear(Base):
    __tablename__ = 'financial_year'

    sl_no = Column(Integer, primary_key=True)
    fin_yr = Column(String, nullable=False)
    cr_yr = Column(String)
    delete_flag = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    working_date = Column(Date)
    running_fin_year = Column(String)


class ForwardTo(Base):
    __tablename__ = 'forward_to'

    serial_no = Column(Integer, primary_key=True)
    scheem_code = Column(String, nullable=False)
    seq = Column(Integer, nullable=False)
    seq_desc = Column(String)
    role_code = Column(String)
    decision_point = Column(String, nullable=False)
    decision_point_desc = Column(String)
    to_seq = Column(Integer)
    process_description = Column(String)
    rol = Column(String)
    dept_code = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String)


class FundBooking(Base):
    __tablename__ = 'fund_booking'

    financial_year = Column(String, nullable=False)
    serial_no = Column(Integer, primary_key=True)
    project_code = Column(Integer)
    account_code = Column(Integer)
    phase = Column(Integer)
    booked_amount = Column(Float)
    actual_expense_amount = Column(Float)
    requisition_no = Column(String)
    requisition_date = Column(Date)
    purchase_order_no = Column(String)
    purchase_oder_date = Column(Date)
    bill_no = Column(String)
    invoice_no = Column(String)
    invoice_date = Column(Date)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    vendor_code = Column(String)
    remarks = Column(String)
    freeze_flag = Column(String)
    freeze_remarks = Column(String)
    reject_remarks = Column(String)
    sric_date = Column(Date)
    fdf_ddf = Column(String)
    purchase_type = Column(String, nullable=False)
    hsn_sac = Column(String)
    gst_rate = Column(Numeric)
    reverse_charges = Column(String, nullable=False)
    goods_or_service = Column(String, nullable=False)
    base_value = Column(Numeric)
    inst_ref_no = Column(String)
    is_gem_purchase_flag = Column(String, nullable=False)
    gem_non_availability_cert_no = Column(String)
    non_gem_approving_person = Column(String)
    non_gem_approving_date = Column(Date)
    demand_no = Column(String)


class GrantDistribution(Base):
    __tablename__ = 'grant_distribution'

    sl_no = Column(Integer, primary_key=True)
    phase_yr = Column(Integer, nullable=False)
    project_code = Column(Integer, nullable=False)
    from_date = Column(Date)
    to_date = Column(Date)
    amount = Column(Numeric)
    remarks = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(String)
    voucher_no = Column(String)
    receipt_no = Column(Integer)
    revert_remark = Column(String)


class GrantDistributionDetails(Base):
    __tablename__ = 'grant_distribution_details'

    sl_no = Column(Integer, primary_key=True)
    phase_yr = Column(Integer, nullable=False)
    project_code = Column(Integer, nullable=False)
    account_code = Column(Integer, nullable=False)
    amount = Column(Numeric)
    remarks = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(String)
    voucher_no = Column(String)
    receipt_no = Column(Integer)


class GrantDistributionDetailsHistory(Base):
    __tablename__ = 'grant_distribution_details_history'

    sl_no = Column(Integer, primary_key=True)
    phase_yr = Column(Integer, nullable=False)
    project_code = Column(Integer, nullable=False)
    account_code = Column(Integer, nullable=False)
    amount = Column(Numeric)
    remarks = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    voucher_no = Column(String)
    receipt_no = Column(Integer)


class GrnMappingWithBill(Base):
    __tablename__ = 'grn_mapping_with_bill'

    project_code = Column(Integer, primary_key=True)
    sric_po_no = Column(String, nullable=False)
    bill_no = Column(String, nullable=False)
    grn = Column(String, nullable=False)
    remarks = Column(String)
    status = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)


class GstLedger(Base):
    __tablename__ = 'gst_ledger'

    org_id = Column(String, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    transaction_type = Column(String, nullable=False)
    transaction_date = Column(Date)
    financial_year = Column(String, nullable=False)
    project_id = Column(Integer)
    vendor_code = Column(String)
    ref_no = Column(String, nullable=False)
    reverse_charges = Column(String, nullable=False)
    base_value = Column(Numeric)
    dr_head = Column(Integer, nullable=False)
    dr_amount = Column(Numeric)
    cr_head = Column(Integer, nullable=False)
    cr_amount = Column(Numeric)
    status = Column(String, nullable=False)
    reconciliation_flag = Column(String, nullable=False)
    input_credit_date = Column(Date)
    input_credit_by = Column(String)
    input_credited_date = Column(Date)
    remarks = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    demand_no = Column(String)
    reconciliation_remarks = Column(String)
    reconciliation_date = Column(DateTime)
    reconciled_by = Column(String)


class GuidStakeholderMap(Base):
    __tablename__ = 'guid_stakeholder_map'

    uid = Column(String)
    serial_no = Column(Integer, primary_key=True)
    stakeholder_type = Column(String)
    stakeholder_code = Column(String)
    updated_by = Column(String)
    update_date = Column(Date)
    can_login_flag = Column(String)


class HallMaster(Base):
    __tablename__ = 'hall_master'

    hallcode = Column(String, primary_key=True)
    hall_name = Column(String)
    gender = Column(String)
    active_flag = Column(String)


class HallRoomAllocation(Base):
    __tablename__ = 'hall_room_allocation'

    rollno = Column(String, primary_key=True)
    sl_no = Column(Numeric)
    hallcode = Column(String)
    block = Column(String)
    room_no = Column(String)
    bed_no = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(Date)
    action_code = Column(String)
    updated_by = Column(String)
    updation_date = Column(Date)
    initiated_by_hmc = Column(String)
    phy_hand_over = Column(String)
    attachment = Column(String)


class HallRoomMaster(Base):
    __tablename__ = 'hall_room_master'

    hallcode = Column(String, primary_key=True)
    block = Column(String)
    room_no = Column(String)
    room_type = Column(String)
    capacity = Column(Numeric)
    floor = Column(Numeric)
    active_flag = Column(Boolean)
    remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    bed_rate = Column(String)
    is_meter_reading_applicable = Column(String)
    hmc_fee = Column(Numeric)


class HallRoomTypeMaster(Base):
    __tablename__ = 'hall_room_type_master'

    room_type = Column(String, primary_key=True)
    display_order = Column(Integer)


class HonorariumConsultancy(Base):
    __tablename__ = 'honorarium_consultancy'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    account_code = Column(String, nullable=False)
    payee_type = Column(String, nullable=False)
    payee_id = Column(String, nullable=False)
    payee_name = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    hours = Column(Integer)
    amount = Column(Numeric)
    remarks = Column(String)
    bank_name = Column(String)
    bank_address = Column(String)
    bank_ifsc_code = Column(String)
    account_no = Column(String)
    pan_no = Column(String)
    status = Column(String)
    competent_auth_remarks = Column(String)
    bill_no = Column(String)
    booking_id = Column(String)
    recovary_head = Column(Integer)
    recovary_amount = Column(Numeric)
    technical_report_status = Column(String)
    technical_report_date = Column(Date)
    eoffice_appv_no = Column(String)
    eoffice_appv_date = Column(Date)
    budgeted_head = Column(Integer)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modified_date = Column(DateTime)
    deleted_flag = Column(String, nullable=False)
    other_recovary_head = Column(Integer)
    other_recovary_amount = Column(Numeric, nullable=False)
    pan_verified_flag = Column(String)
    pan_verified_by = Column(String)
    pan_verified_ts = Column(DateTime)
    tech_report_file_ref = Column(String)
    head_dean_file_ref = Column(String)
    pi = Column(String)
    pi_date = Column(DateTime)


class HonorariumConsultancyHistory(Base):
    __tablename__ = 'honorarium_consultancy_history'

    serial_no = Column(Integer, primary_key=True)
    sl_no = Column(Integer, nullable=False)
    financial_year = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    account_code = Column(String, nullable=False)
    payee_type = Column(String, nullable=False)
    payee_id = Column(String, nullable=False)
    payee_name = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    hours = Column(Integer)
    amount = Column(Numeric)
    remarks = Column(String)
    bank_name = Column(String)
    bank_address = Column(String)
    bank_ifsc_code = Column(String)
    account_no = Column(String)
    pan_no = Column(String)
    status = Column(String)
    competent_auth_remarks = Column(String)
    bill_no = Column(String)
    booking_id = Column(String)
    technical_report_status = Column(String)
    technical_report_date = Column(Date)
    created_by = Column(String)
    creation_date = Column(DateTime)
    budgeted_head = Column(Integer)
    pi = Column(String)
    pi_date = Column(DateTime)


class ImgMaster(Base):
    __tablename__ = 'img_master'

    stakeholder_code = Column(String, primary_key=True)
    stakeholder_type = Column(String)
    img_code = Column(String)
    slno = Column(Integer)
    img_path = Column(String)
    upload_date = Column(DateTime)
    uploded_by = Column(String)
    image_name = Column(String)
    delete_flag = Column(String)
    overwritten = Column(Boolean)


class IndvBalance(Base):
    __tablename__ = 'indv_balance'

    financial_year = Column(String, nullable=False)
    empno = Column(String, nullable=False)
    op_balance = Column(Numeric)
    receipt_amount = Column(Numeric)
    payment_amount = Column(Numeric)
    cl_balance = Column(Numeric)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    chart_of_account = Column(String, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    ref_no = Column(Integer)
    ref_type = Column(String)
    ref_financial_yr = Column(String)
    remarks = Column(String)
    edit_remarks = Column(String)


class ItaxOutsideDeclaration(Base):
    __tablename__ = 'itax_outside_declaration'

    fin_year = Column(String, primary_key=True)
    empno = Column(String, nullable=False)
    item_code = Column(Integer, nullable=False)
    amount = Column(Numeric)
    created_by = Column(String)
    creation_time = Column(DateTime)
    updated_by = Column(String)
    updation_time = Column(DateTime)
    ver_amount = Column(Numeric)
    lock_flag = Column(String)
    verified_flag = Column(String)


class ItaxOutsideDeclarationItems(Base):
    __tablename__ = 'itax_outside_declaration_items'

    item_code = Column(Integer, nullable=False)
    under_section = Column(String)
    description = Column(String)
    remarks = Column(String)
    fin_year = Column(String, primary_key=True)
    doc_ver_reqd = Column(String)
    doc_reqd = Column(String)
    max_limit = Column(String)
    disp_serial = Column(String)


class Itaxrate(Base):
    __tablename__ = 'itaxrate'

    finyear = Column(String, primary_key=True)
    sex = Column(String, nullable=False)
    from_amt = Column(Numeric, nullable=False)
    to_amt = Column(Numeric, nullable=False)
    rate = Column(Numeric, nullable=False)
    min_amt = Column(Numeric, nullable=False)
    surcharge = Column(Numeric, nullable=False)
    cess = Column(Numeric, nullable=False)


class JournalVoucher(Base):
    __tablename__ = 'journal_voucher'

    fin_year = Column(String, primary_key=True)
    project_code = Column(Integer, nullable=False)
    sl_no = Column(Integer, nullable=False)
    jvno = Column(String, nullable=False)
    jv_date = Column(Date)
    jv_type = Column(String, nullable=False)
    jv_ref_no = Column(String, nullable=False)
    dr_head_id = Column(Integer)
    dr_amt = Column(Numeric)
    cr_head_id = Column(Integer)
    cr_amt = Column(Numeric)
    remarks = Column(String, nullable=False)
    delete_flag = Column(String)
    created_by = Column(String, nullable=False)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    freeze_flag = Column(String, nullable=False)
    dept = Column(String)
    reverse_flag = Column(String, nullable=False)


class LeaveApplicationForProjectStaff(Base):
    __tablename__ = 'leave_application_for_project_staff'

    sl_no = Column(Integer, primary_key=True)
    leave_year = Column(String, nullable=False)
    application_no = Column(String)
    project_code = Column(Integer)
    sric_id = Column(String, nullable=False)
    type_of_leave = Column(String)
    leave_from_date = Column(Date)
    leave_from_time = Column(String)
    leave_to_date = Column(Date)
    leave_to_time = Column(String)
    station_leaving_from_date = Column(Date)
    station_leaving_from_time = Column(String)
    station_leaving_to_date = Column(Date)
    station_leaving_to_time = Column(String)
    purpose_of_leave = Column(String)
    leave_arrangement_by = Column(String)
    address_during_leave = Column(String)
    status = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    pi_guide_id = Column(String)


class LeaveApplicationForProjectStaffHistory(Base):
    __tablename__ = 'leave_application_for_project_staff_history'

    hist_sl_no = Column(Integer, nullable=False)
    leave_year = Column(String)
    application_no = Column(String, nullable=False)
    project_code = Column(Integer, primary_key=True)
    sric_id = Column(String)
    type_of_leave = Column(String)
    leave_from_date = Column(Date)
    leave_from_time = Column(String)
    leave_to_date = Column(Date)
    leave_to_time = Column(String)
    station_leaving_from_date = Column(Date)
    station_leaving_from_time = Column(String)
    station_leaving_to_date = Column(Date)
    station_leaving_to_time = Column(String)
    purpose_of_leave = Column(String)
    leave_arrangement_by = Column(String)
    address_during_leave = Column(String)
    status = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    pi_guide_id = Column(String)


class ModuleConfigurationDetails(Base):
    __tablename__ = 'module_configuration_details'

    parameter_name = Column(String, primary_key=True)
    parameter_value = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)


class ModuleUserMaster(Base):
    __tablename__ = 'module_user_master'

    user_code = Column(String, primary_key=True)
    user_type = Column(String, nullable=False)
    password = Column(String, nullable=False)
    public_key = Column(String)
    private_key = Column(String)
    activated_from = Column(Date)
    activated_to = Column(Date)
    access_flag = Column(Boolean)
    created_by = Column(String)
    creation_date = Column(Date)
    approved_by = Column(String)
    approval_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    alias = Column(String)
    sign_expiry_date = Column(Date)
    alias_password = Column(String)
    user_detail_code = Column(String)
    signedflag = Column(String)


class NoDemandCertificate(Base):
    __tablename__ = 'no_demand_certificate'

    sl_no = Column(Integer, primary_key=True)
    sric_id = Column(String, nullable=False)
    no_demand_certificate_id = Column(String, nullable=False)
    desg_id = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    dept_id = Column(String, nullable=False)
    from_date = Column(Date, nullable=False)
    exp_to_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    remarks = Column(String)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    future_address = Column(String)
    future_contact_no = Column(String)
    medical_book_surrender = Column(String, nullable=False)
    sric_id_card_surrender = Column(String, nullable=False)
    hall_code = Column(String)
    ndc_type = Column(String, nullable=False)
    ref_id = Column(String)


class NoDemandCertificateHistory(Base):
    __tablename__ = 'no_demand_certificate_history'

    serial_no = Column(Integer, primary_key=True)
    sric_id = Column(String, nullable=False)
    no_demand_certificate_id = Column(String, nullable=False)
    desg_id = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    dept_id = Column(String, nullable=False)
    from_date = Column(Date, nullable=False)
    exp_to_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    remarks = Column(String)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)


class OldProjectBalanceAdjustment(Base):
    __tablename__ = 'old_project_balance_adjustment'

    sl_no = Column(Integer, primary_key=True)
    project_type = Column(String, nullable=False)
    project_code = Column(String, nullable=False)
    tally_balance_31_03_2013 = Column(Numeric)
    erp_balance_31_03_2013 = Column(Numeric)
    erp_balance_28_11_2021 = Column(Numeric)
    diff_of_opening_balance_tally_erp = Column(Numeric)
    revised_closing_balance_would_be_28112021 = Column(Numeric)
    upload_date = Column(Date)
    delete_flag = Column(String, nullable=False)


class OutsourceAdvertisementDetails(Base):
    __tablename__ = 'outsource_advertisement_details'

    sl_no = Column(Integer, primary_key=True)
    project = Column(String, nullable=False)
    designation = Column(String)
    adv_last_date = Column(Date)
    adv_link = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    financial_year = Column(String, nullable=False)
    remarks = Column(String)
    status = Column(String, nullable=False)
    adv_file = Column(LargeBinary)


class ProjectAreaCouncil(Base):
    __tablename__ = 'project_area_council'

    area_id = Column(String, primary_key=True)
    description = Column(String)
    involving_dept = Column(String)
    delete_flag = Column(String, nullable=False)


class ProjectCoordinatingDept(Base):
    __tablename__ = 'project_coordinating_dept'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Numeric, nullable=False)
    dept_code = Column(String, nullable=False)
    remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(String)
    delete_flag = Column(String, nullable=False)


class ProjectCreation(Base):
    __tablename__ = 'project_creation'

    sl_no = Column(Integer, primary_key=True)
    proposal_id = Column(String)
    financial_year = Column(String, nullable=False)
    project_title = Column(String)
    project_type = Column(String)
    mode_of_grant = Column(String)
    date_of_commencement = Column(Date)
    date_of_closing = Column(Date)
    project_value = Column(Numeric)
    sponsor_letter_no = Column(String)
    sponsor_letter_date = Column(Date)
    project_technology = Column(String)
    proposal_abstract = Column(String)
    status = Column(String)
    step = Column(Integer)
    freeze_flag = Column(String, nullable=False)
    created_by = Column(String, nullable=False)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    consultancy_project_involves = Column(String)
    foreign_travel = Column(String, nullable=False)
    tech_dev_tranfer = Column(String)
    project_code = Column(Integer)
    project_id = Column(String)
    proposal_to_project_flag = Column(String, nullable=False)
    justification_proposal_involves = Column(String)
    status_remarks = Column(String)
    status_created_by = Column(String)
    status_creation_date = Column(DateTime)
    project_scheme = Column(String)
    project_duration = Column(Integer)
    keywords = Column(String)
    freeze_ts = Column(DateTime)
    hours_spent = Column(String)
    forward_remarks = Column(String)


class ProjectCreationDept(Base):
    __tablename__ = 'project_creation_dept'

    sl_no = Column(Integer, primary_key=True)
    dept = Column(String, nullable=False)
    deptname = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    modified_by = Column(String)
    modification_date = Column(String)
    proposal_id = Column(String, nullable=False)


class ProjectDelegateToOthers(Base):
    __tablename__ = 'project_delegate_to_others'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    assignee_type = Column(String, nullable=False)
    assignee_to = Column(String, nullable=False)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date)
    access_flag = Column(String, nullable=False)
    remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    process_type = Column(String, nullable=False)


class ProjectExpectedReceiptDetails(Base):
    __tablename__ = 'project_expected_receipt_details'

    expected_receipt_no = Column(Integer)
    project_code = Column(Integer, primary_key=True)
    installment_no = Column(Integer)
    expected_receipt_amount = Column(Integer)
    expected_receipt_date = Column(Date)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)


class ProjectExtractionDataForUc(Base):
    __tablename__ = 'project_extraction_data_for_uc'

    transaction_type = Column(String, nullable=False)
    ref_no = Column(String, nullable=False)
    project_code = Column(Integer, primary_key=True)
    ext_from_date = Column(Date, nullable=False)
    ext_to_date = Column(Date, nullable=False)
    parent_account_code = Column(Integer)
    account_code = Column(Integer)
    map_account_code = Column(Integer)
    dr_amount = Column(Numeric)
    cr_amount = Column(Numeric)
    status = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    remarks = Column(String)
    transaction_date = Column(Date, nullable=False)
    phase = Column(Integer)
    receipt_details_no = Column(Integer, nullable=False)


class ProjectExtractionDataGfrForUc(Base):
    __tablename__ = 'project_extraction_data_gfr_for_uc'

    project_code = Column(Integer, primary_key=True)
    phase = Column(Integer, nullable=False)
    expenditure_type = Column(String, nullable=False)
    op_balance = Column(Float)
    receipt_amount = Column(Float)
    payment_amount = Column(Float)
    cl_balance = Column(Float)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modified_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    account_code = Column(String, nullable=False)


class ProjectExtractionInterestJvForUc(Base):
    __tablename__ = 'project_extraction_interest_jv_for_uc'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    from_date = Column(Date)
    to_date = Column(Date)
    page_no = Column(Integer)
    remarks = Column(String)
    amount = Column(Float)
    remarks_ordering = Column(Integer)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    status = Column(String, nullable=False)
    account_type = Column(String)
    scheme = Column(String)


class ProjectFileUpload(Base):
    __tablename__ = 'project_file_upload'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    doc_phy_path = Column(String)
    remarks = Column(String)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    doc_type = Column(String)
    file = Column(LargeBinary)
    upload_user_type = Column(String, nullable=False)
    file_share = Column(String, nullable=False)
    lock_flag = Column(String)
    ref_no = Column(String)


class ProjectInchargeDetails(Base):
    __tablename__ = 'project_incharge_details'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    emp_code = Column(String, nullable=False)
    emp_type = Column(String, nullable=False)
    active_from = Column(Date)
    active_to = Column(Date)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    remarks = Column(String)
    department = Column(String)
    initial_invt_desg = Column(String)
    copy_to = Column(String)
    share_flag = Column(String)
    special_remarks = Column(String)


class ProjectInchargeDetailsHistory(Base):
    __tablename__ = 'project_incharge_details_history'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    emp_code = Column(String, nullable=False)
    emp_type = Column(String, nullable=False)
    active_from = Column(Date)
    active_to = Column(Date)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    remarks = Column(String)
    department = Column(String)
    initial_invt_desg = Column(String)
    copy_to = Column(String)
    special_remarks = Column(String)


class ProjectLeaveError(Base):
    __tablename__ = 'project_leave_error'

    error = Column(String, primary_key=True)
    creation_time = Column(DateTime)


class ProjectMaster(Base):
    __tablename__ = 'project_master'

    user_project_code = Column(String)
    project_type = Column(String)
    title = Column(String)
    sanction_letter_no = Column(String)
    sanction_letter_date = Column(Date)
    total_sanctioned_grant = Column(Float)
    date_of_commencement = Column(Date)
    duration = Column(Numeric)
    mode_of_payment = Column(String)
    institute_approval_no = Column(String)
    expertise_availability_flag = Column(String)
    expertise_availability_remarks = Column(String)
    facility_availability_flag = Column(String)
    facility_availability_remarks = Column(String)
    dac_approval_flag = Column(String)
    hod_approval_flag = Column(String)
    ar_sric_approval_flag = Column(String)
    dean_sric_approval_flag = Column(String)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    research_dept_code = Column(String)
    project_code = Column(Integer, primary_key=True)
    con_pro_fac_used = Column(Float)
    rejection_remarks = Column(String)
    rejection_flag = Column(String)
    pending_to = Column(String)
    closing_date = Column(Date)
    institute_approval_dt = Column(Date)
    consultancy_project_type = Column(String)
    sanctioned_authority = Column(String)
    sanc_auth_dt = Column(Date)
    acc_no = Column(String)
    remarks = Column(String)
    financial_year = Column(String)
    sric_cl_flg = Column(String)
    sric_cl_date = Column(Date)
    sric_cl_remarks = Column(String)
    project_belongs = Column(String)
    file_name = Column(String)
    file_path = Column(String)
    date_of_filing = Column(DateTime)
    signed_by = Column(String)
    signed_flag = Column(String)
    doc_id = Column(String)
    send_mail = Column(String)
    co_dept_flag = Column(String)
    scheem_type = Column(String)
    close_flag = Column(String, nullable=False)
    prov_cl_flag = Column(String)
    prov_cl_date = Column(DateTime)
    prov_cl_remarks = Column(String)
    share_flag = Column(String)
    claim_input_credit_project = Column(String)
    claim_input_credit_project_date = Column(DateTime)
    comp_auth = Column(String)
    sric_virtual_project_flag = Column(String)
    project_insufficient_balance_flag = Column(String, nullable=False)
    sent_mail_count_for_insufficient_project_balance = Column(Integer)
    mail_sent_date_for_project_insufficient_balance = Column(DateTime)
    project_stopped_status = Column(String, nullable=False)
    project_stopped_by = Column(String)
    project_stopped_date = Column(DateTime)
    project_stopped_remarks = Column(String)
    collaborative_project = Column(String, nullable=False)
    inst_type_project = Column(String, nullable=False)
    inst_type_created_by = Column(String)
    inst_type_creation_date = Column(DateTime)
    inst_type_remarks = Column(String)
    unbounded_fund_flag = Column(String, nullable=False)
    project_extended_flag = Column(String, nullable=False)
    project_extended_remarks = Column(String)
    from_extended_date = Column(Date)
    extended_by = Column(String)
    sponsor_closing_date = Column(Date)
    hra = Column(String)
    fellowship_project = Column(String, nullable=False)
    hours_spent = Column(String)
    ovh_dist = Column(String, nullable=False)
    non_recurring_fund_unbounded_flag = Column(String, nullable=False)
    project_unfounded_flag = Column(String, nullable=False)
    csr_flag = Column(String, nullable=False)
    ovh_remarks = Column(String)


class ProjectMasterHistory(Base):
    __tablename__ = 'project_master_history'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    user_project_code = Column(String)
    project_type = Column(String)
    title = Column(String)
    research_dept_code = Column(String)
    sanction_letter_no = Column(String)
    sanction_letter_date = Column(Date)
    total_sanctioned_grant = Column(Float)
    date_of_commencement = Column(Date)
    closing_date = Column(Date)
    duration = Column(Numeric)
    mode_of_payment = Column(String)
    institute_approval_no = Column(String)
    rejection_remarks = Column(String)
    rejection_flag = Column(String)
    pending_to = Column(String)
    institute_approval_dt = Column(Date)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    remarks = Column(String)
    consultancy_project_type = Column(String)
    sanctioned_authority = Column(String)
    sanc_auth_dt = Column(Date)
    acc_no = Column(String)
    financial_year = Column(String)
    sric_cl_flg = Column(String)
    sric_cl_date = Column(Date)
    sric_cl_remarks = Column(String)
    project_belongs = Column(String)
    file_name = Column(String)
    file_path = Column(String)
    date_of_filing = Column(DateTime)
    signed_by = Column(String)
    signed_flag = Column(String)
    doc_id = Column(String)
    send_mail = Column(String)
    co_dept_flag = Column(String)
    scheem_type = Column(String)
    comp_auth = Column(String)
    sric_virtual_project_flag = Column(String)
    project_insufficient_balance_flag = Column(String, nullable=False)
    sent_mail_count_for_insufficient_project_balance = Column(Integer)
    mail_sent_date_for_project_insufficient_balance = Column(DateTime)
    inst_type_project = Column(String, nullable=False)
    project_stopped_status = Column(String, nullable=False)
    project_stopped_by = Column(String)
    project_stopped_date = Column(DateTime)
    project_stopped_remarks = Column(String)
    collaborative_project = Column(String, nullable=False)
    unbounded_fund_flag = Column(String, nullable=False)
    project_extended_flag = Column(String, nullable=False)
    project_extended_remarks = Column(String)
    from_extended_date = Column(Date)
    extended_by = Column(String)
    close_flag = Column(String, nullable=False)
    sponsor_closing_date = Column(Date)
    hra = Column(String)
    fellowship_project = Column(String, nullable=False)
    hours_spent = Column(String)
    ovh_dist = Column(String, nullable=False)
    non_recurring_fund_unbounded_flag = Column(String, nullable=False)
    csr_flag = Column(String, nullable=False)
    project_unfounded_flag = Column(String, nullable=False)
    ovh_remarks = Column(String)


class ProjectMasterIndv(Base):
    __tablename__ = 'project_master_indv'

    roll_no = Column(String, primary_key=True)
    user_project_code = Column(String)
    project_type = Column(String)
    title = Column(String)
    sanction_letter_no = Column(String)
    sanction_letter_date = Column(Date)
    total_sanctioned_grant = Column(Float)
    date_of_joining = Column(Date)
    duration = Column(Numeric)
    closing_date = Column(Date)
    institute_approval_no = Column(String)
    institute_approval_dt = Column(Date)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    research_dept_code = Column(String)
    pending_to = Column(String)
    acc_no = Column(String)
    remarks = Column(String)
    financial_year = Column(String)
    termination_date = Column(DateTime)
    sponsor_file_name = Column(String)
    sponsor_doc_phy_path = Column(String)
    sponsor_code = Column(String)


class ProjectPhaseDuration(Base):
    __tablename__ = 'project_phase_duration'

    project_code = Column(Integer, primary_key=True)
    phase = Column(Integer, nullable=False)
    from_date = Column(Date)
    to_date = Column(Date)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    delete_flag = Column(String)


class ProjectProposalCallName(Base):
    __tablename__ = 'project_proposal_call_name'

    sl_no = Column(Numeric, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String)
    delete_flag = Column(String, nullable=False)


class ProjectProposalMaster(Base):
    __tablename__ = 'project_proposal_master'

    proposal_code = Column(Integer, primary_key=True)
    proposal_version = Column(Float, nullable=False)
    proposal_user_code = Column(String, nullable=False)
    title = Column(String, nullable=False)
    project_type = Column(String, nullable=False)
    brief_overview = Column(String)
    status = Column(String, nullable=False)
    duration = Column(Integer)
    doc_phy_path = Column(String)
    remarks = Column(String)
    acceptance_flag = Column(String, nullable=False)
    acceptance_date = Column(Date)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String, nullable=False)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    project_cost = Column(Numeric)
    approval_order_no = Column(String)
    approval_doc_path = Column(String)
    expected_maturity_date = Column(Date)
    approved_amount = Column(Numeric)
    sponsor_letter_no = Column(String)
    principal_investigator = Column(String)
    co_pi = Column(String)
    department = Column(String)
    pi_code = Column(String)
    sponsor_acceptance_date = Column(Date)
    closing_date = Column(Date)
    approval_order_dt = Column(Date)
    sponsor_copy_no = Column(Integer)


class ProjectProposalMasterTemp(Base):
    __tablename__ = 'project_proposal_master_temp'

    proposal_code = Column(Integer, primary_key=True)
    proposal_version = Column(Float, nullable=False)
    proposal_user_code = Column(String, nullable=False)
    title = Column(String, nullable=False)
    project_type = Column(String, nullable=False)
    brief_overview = Column(String)
    status = Column(String, nullable=False)
    duration = Column(Integer)
    doc_phy_path = Column(String)
    remarks = Column(String)
    acceptance_flag = Column(String, nullable=False)
    acceptance_date = Column(Date)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String, nullable=False)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    project_cost = Column(Numeric)
    approval_order_no = Column(String)
    approval_doc_path = Column(String)
    expected_maturity_date = Column(Date)
    approved_amount = Column(Numeric)
    sponsor_letter_no = Column(String)
    principal_investigator = Column(String)
    co_pi = Column(String)
    department = Column(String)
    pi_code = Column(String)
    sponsor_acceptance_date = Column(Date)
    closing_date = Column(Date)
    approval_order_dt = Column(Date)
    sponsor_copy_no = Column(Integer)


class ProjectProposalSponsorDetail(Base):
    __tablename__ = 'project_proposal_sponsor_detail'

    proposal_user_code = Column(String, nullable=False)
    proposal_version = Column(Float, nullable=False)
    sponsor_code = Column(String)
    sponsor_name = Column(String)
    sponsor_type = Column(String)
    full_address = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    contact_no = Column(String)
    e_mail = Column(String)
    proposal_code = Column(Integer)
    serial_no = Column(Integer, primary_key=True)


class ProjectSponsorDetails(Base):
    __tablename__ = 'project_sponsor_details'

    sponsor_code = Column(Integer, nullable=False)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    project_code = Column(Integer, primary_key=True)
    serial_no = Column(Integer, nullable=False)
    roll_no = Column(String)


class ProjectStaffDependentList(Base):
    __tablename__ = 'project_staff_dependent_list'

    sric_id = Column(String, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    aadhaar_id_no = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    dependent_name = Column(String, nullable=False)
    dob = Column(Date)
    gender = Column(String, nullable=False)
    relation = Column(String, nullable=False)
    facilities_status = Column(String, nullable=False)
    remarks = Column(String, nullable=False)
    appv_flag = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    facility_type = Column(String, nullable=False)
    creation_date = Column(DateTime)
    identity_type = Column(String)


class ProjectStaffIdCardRequest(Base):
    __tablename__ = 'project_staff_id_card_request'

    slno = Column(Numeric, nullable=False)
    empno = Column(String, nullable=False)
    project_code = Column(Integer, primary_key=True)
    remarks = Column(String)
    status = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)


class ProjectStaffMaster(Base):
    __tablename__ = 'project_staff_master'

    new_empno = Column(String, nullable=False)
    empname = Column(String)
    emp_sex = Column(String)
    emp_maritalsts = Column(String)
    emp_father = Column(String)
    emp_prsadd = Column(String)
    emp_pmtadd = Column(String)
    emp_edu = Column(String)
    emp_pedu = Column(String)
    emp_cast = Column(String)
    empbasic = Column(Float)
    emp_lastbasic = Column(Float)
    empdob = Column(Date)
    empdoj = Column(Date)
    time_join = Column(String)
    empdor = Column(DateTime)
    empdesg = Column(String)
    empdept = Column(String)
    in_service = Column(String)
    pan_no = Column(String)
    bank_code = Column(String)
    account_no = Column(String)
    project_title = Column(String)
    empdol = Column(Date)
    office_orderno = Column(String)
    office_orderdate = Column(Date)
    staff_type = Column(String)
    payment_type = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    project_code = Column(Integer, primary_key=True)
    delete_flag = Column(String, nullable=False)
    roll_no = Column(String)
    ref_empno = Column(String)
    pi_copi = Column(String)
    through = Column(String)
    ext_type = Column(String)
    from_empdesg = Column(String)
    dept = Column(String)
    from_project_code = Column(Integer)
    from_pi_copi = Column(String)
    joining_confirmation = Column(String)
    appl_no = Column(String)
    empno = Column(String)
    blood_gr = Column(String)
    emergency_contact_no = Column(String)
    emergency_contact_address = Column(String)
    emergency_contact_person = Column(String)
    emergency_person_relationship = Column(String)
    emp_mail_id = Column(String)
    emp_contact_no = Column(String)
    name_photo = Column(String)
    name_sign = Column(String)
    time_termination_resignation = Column(String)
    term_reg_dt = Column(Date)
    nationality = Column(String)
    emp_type = Column(String)
    arrear = Column(Numeric)
    ptax = Column(Numeric)
    itax = Column(Numeric)
    vsrc = Column(Numeric)
    lfees = Column(Numeric)
    electric = Column(Numeric)
    misc = Column(Numeric)
    guidance_flag = Column(String)
    scale_ind = Column(String)
    batch_flg = Column(String)
    batch_dt = Column(DateTime)
    yr = Column(String)
    mnth = Column(String)
    netpay = Column(String)
    remarks = Column(String)
    page = Column(String)
    bank_name = Column(String)
    bank_address = Column(String)
    micr = Column(String)
    bank_remarks = Column(String)
    ppf = Column(Numeric)
    hra = Column(Numeric)
    lock_flag = Column(String)
    lock_remarks = Column(String)
    pre_from_date = Column(Date)
    pre_to_date = Column(Date)
    pre_amount = Column(Float)
    next_from_date = Column(Date)
    next_to_date = Column(Date)
    next_amount = Column(Float)
    vsrc_flag = Column(String, nullable=False)
    role_desg = Column(String)
    role_desg_desc = Column(String)
    online_flag = Column(String, nullable=False)
    demand_no = Column(String)
    refund_hra_amount = Column(Numeric)
    generated_otp = Column(String)
    otp_generation_time = Column(DateTime)
    otp_count = Column(Numeric)
    booking_id = Column(String)
    paper_verify_flag = Column(String)
    joining_doc_id = Column(String)
    doc_created_by = Column(String)
    doc_creation_date = Column(DateTime)
    hmc_charges = Column(Numeric)
    onrole_student = Column(String, nullable=False)
    uid = Column(String)


class ProjectStaffMasterHistory(Base):
    __tablename__ = 'project_staff_master_history'

    sl_no = Column(Integer, primary_key=True)
    empno = Column(String, nullable=False)
    empname = Column(String)
    emp_sex = Column(String)
    emp_maritalsts = Column(String)
    emp_father = Column(String)
    emp_prsadd = Column(String)
    emp_pmtadd = Column(String)
    emp_edu = Column(String)
    emp_pedu = Column(String)
    emp_cast = Column(String)
    blood_group = Column(String)
    empbasic = Column(Float)
    emp_lastbasic = Column(Float)
    empdob = Column(Date)
    empdoj = Column(Date)
    time_join = Column(String)
    empdni = Column(DateTime)
    empdor = Column(DateTime)
    empdesg = Column(String)
    empsubpst = Column(String)
    emp_inidesgn = Column(String)
    empdept = Column(String)
    empclas = Column(String)
    place_of_posting = Column(String)
    hra_flag = Column(String)
    npa_flag = Column(String)
    handy_flag = Column(String)
    empstatus = Column(String)
    eol_status = Column(String)
    on_deputation = Column(String)
    salcode = Column(String)
    salsrno = Column(String)
    empbankac = Column(String)
    pay_yn = Column(String)
    pftype = Column(String)
    scale_ind = Column(String)
    eb_flag = Column(String)
    punish_flag = Column(String)
    on_prob = Column(String)
    con_dt = Column(DateTime)
    prob_prd = Column(String)
    promot_dt = Column(DateTime)
    elcrdt = Column(Float)
    hplcrdt = Column(Float)
    emplstincdt = Column(DateTime)
    vactype = Column(String)
    lastpromodt = Column(DateTime)
    dt_reg_exp = Column(DateTime)
    oo_no_dt = Column(String)
    appt_type = Column(String)
    sal_status = Column(String)
    religion = Column(String)
    last_prom_dt = Column(DateTime)
    place_birth = Column(String)
    in_service = Column(String)
    file_no = Column(String)
    specialisation1 = Column(String)
    specialisation2 = Column(String)
    pan_no = Column(String)
    bank_code = Column(String)
    account_no = Column(String)
    net_salary = Column(Float)
    rspf_gpf = Column(Float)
    group_insurance = Column(Float)
    house_rent = Column(Float)
    festival_advance = Column(Float)
    professional_tax = Column(Float)
    lic_premium = Column(Float)
    staff_club = Column(Float)
    technology_club = Column(Float)
    co_op_credit_society = Column(Float)
    furniture_rent = Column(Float)
    house_building_advance = Column(Float)
    transport_advance = Column(Float)
    guest_house = Column(Float)
    hospital_charge = Column(Float)
    income_tax_surcharge = Column(Float)
    vsrc_sric_account = Column(Float)
    tech_film_society = Column(Float)
    miscellaneous = Column(Float)
    project_title = Column(String)
    department = Column(String)
    dedution_total = Column(Float)
    total_gross = Column(Float)
    empdol = Column(Date)
    office_orderno = Column(String)
    office_orderdate = Column(Date)
    staff_type = Column(String)
    payment_type = Column(String)
    payment_mode = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    pan = Column(String)
    project_code = Column(Integer)
    delete_flag = Column(String, nullable=False)
    roll_no = Column(String)
    ref_empno = Column(String)
    pi_copi = Column(String)
    through = Column(String)
    ext_type = Column(String)
    from_empdesg = Column(String)
    dept = Column(String)
    from_project_code = Column(Integer)
    from_pi_copi = Column(String)
    joining_confirmation = Column(String)
    blood_gr = Column(String)
    conact_no = Column(String)
    emergency_contact_no = Column(String)
    emergency_contact_address = Column(String)
    emergency_contact_person = Column(String)
    emergency_person_relationship = Column(String)
    emp_mail_id = Column(String)
    emp_contact_no = Column(String)
    name_photo = Column(String)
    name_sign = Column(String)
    new_empno = Column(String)
    time_termination_resignation = Column(String)
    term_reg_dt = Column(Date)
    pre_from_date = Column(Date)
    pre_to_date = Column(Date)
    pre_amount = Column(Float)
    next_from_date = Column(Date)
    next_to_date = Column(Date)
    next_amount = Column(Float)
    vsrc_flag = Column(String, nullable=False)
    role_desg = Column(String)
    role_desg_desc = Column(String)
    joining_doc_id = Column(String)


class ProjectStaffMasterIdCard(Base):
    __tablename__ = 'project_staff_master_id_card'

    empno = Column(String, primary_key=True)
    slno = Column(Numeric, nullable=False)
    dispatched_by = Column(String)
    dispatched_on = Column(DateTime)
    approved_by = Column(String)
    approved_on = Column(DateTime)
    id_card_dispatch_status = Column(String)


class ProjectStaffResignation(Base):
    __tablename__ = 'project_staff_resignation'

    sl_no = Column(Integer, primary_key=True)
    sric_id = Column(String, nullable=False)
    resignation_id = Column(String, nullable=False)
    no_demand_certificate_id = Column(String, nullable=False)
    desg_id = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    dept_id = Column(String, nullable=False)
    date_of_resignation = Column(Date, nullable=False)
    fn_an_of_resignation = Column(String, nullable=False)
    status = Column(String, nullable=False)
    remarks = Column(String)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)


class ProjectStaffResignationHistory(Base):
    __tablename__ = 'project_staff_resignation_history'

    serial_no = Column(Integer, primary_key=True)
    resignation_id = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    date_of_resignation = Column(Date, nullable=False)
    fn_an_of_resignation = Column(String, nullable=False)
    status = Column(String, nullable=False)
    remarks = Column(String)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)


class ProjectStaffSanctionedDetails(Base):
    __tablename__ = 'project_staff_sanctioned_details'

    designation = Column(String, nullable=False)
    consolidated_compensation = Column(Float, nullable=False)
    no_of_post = Column(Numeric, nullable=False)
    remarks = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    project_code = Column(Integer, primary_key=True)


class ProjectSubproject(Base):
    __tablename__ = 'project_subproject'

    project_code = Column(Integer, primary_key=True)
    sub_project_code = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String)


class ProjectTourDetails(Base):
    __tablename__ = 'project_tour_details'

    approval_no = Column(String, nullable=False)
    project_code = Column(Integer, primary_key=True)
    payee_code = Column(String)
    payee_type = Column(String)
    place_of_visit = Column(String)
    purpose_of_visit = Column(String)
    duration_from = Column(Date)
    duration_to = Column(Date)
    adv_amt = Column(Numeric)
    adv_bill_no = Column(String)
    adj_bill_no = Column(String)
    status = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String)
    appv_type = Column(String)
    file_name = Column(String)
    file_path = Column(String)
    workflow_id = Column(String)
    instance_id = Column(Integer)
    remarks = Column(String)
    approve_flag = Column(String)
    approved_by = Column(String)
    approval_time = Column(DateTime)
    inst_appv = Column(String)
    fr_dt_time = Column(String)
    to_dt_time = Column(String)
    pi = Column(String)
    signed_by = Column(String)
    signed_flag = Column(String)
    send_mail = Column(String)
    count_send_mail = Column(Integer)
    date_of_filing = Column(DateTime)
    mailing_date = Column(DateTime)
    signed_file_name = Column(String)
    signed_file_name_path = Column(String)
    dean_signed_by = Column(String)
    dean_signed_date = Column(DateTime)
    dean_signed_flag = Column(String)
    station_leave_from_date = Column(Date)
    station_leave_fromtime = Column(String)
    station_leave_to_date = Column(Date)
    station_leave_totime = Column(String)
    journey_type = Column(String, nullable=False)
    count_reminder_email = Column(Integer)
    reminder_email_send_date = Column(DateTime)
    reminder_send_email_by = Column(String)
    undertaking_content = Column(String)
    undertaking_by = Column(String)
    undertaking_date = Column(DateTime)
    undertaking_flag = Column(String, nullable=False)


class ProjectTourDetailsHistory(Base):
    __tablename__ = 'project_tour_details_history'

    sl_no = Column(Integer, primary_key=True)
    approval_no = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    payee_code = Column(String)
    payee_type = Column(String)
    place_of_visit = Column(String)
    purpose_of_visit = Column(String)
    duration_from = Column(Date)
    duration_to = Column(Date)
    adv_amt = Column(Numeric)
    adv_bill_no = Column(String)
    adj_bill_no = Column(String)
    status = Column(String)
    delete_remarks = Column(String)
    creation_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    adv_flag = Column(String)
    adj_flag = Column(String)
    delete_flag = Column(String)
    hard_copy_received = Column(String)
    hard_copy_received_dt = Column(DateTime)
    ar = Column(String)
    ar_dt = Column(DateTime)
    dean = Column(String)
    dean_dt = Column(DateTime)
    pi_code = Column(String)
    js_remarks = Column(String)
    ar_remarks = Column(String)
    dean_remarks = Column(String)
    reject_remarks = Column(String)


class ProjectTourDetailsOthers(Base):
    __tablename__ = 'project_tour_details_others'

    approval_no = Column(String)
    project_code = Column(Integer, primary_key=True)
    applicant_code = Column(String)
    applicant_name = Column(String)
    appv_type = Column(String)
    approved_by = Column(String, nullable=False)
    place_of_visit = Column(String)
    purpose_of_visit = Column(String)
    duration_from = Column(Date)
    duration_to = Column(Date)
    fr_dt_time = Column(String)
    to_dt_time = Column(String)
    adv_amt = Column(Numeric)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String)
    remarks = Column(String)
    status = Column(String, nullable=False)
    sl_no = Column(Integer, nullable=False)
    email_id = Column(String)
    applicant_type = Column(String)
    applicant_type_actual = Column(String)
    doc_id = Column(String)


class ProjectTypeMaster(Base):
    __tablename__ = 'project_type_master'

    type_code = Column(String, primary_key=True)
    type_desc = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)


class ProjFdfDdfAllBal(Base):
    __tablename__ = 'proj_fdf_ddf_all_bal'

    project_id = Column(String, primary_key=True)
    user_project_code = Column(String)
    cl_balance = Column(String)
    bill_amt = Column(String)
    fund_booking_amt = Column(String)
    in_process_amount = Column(String)
    effective_balance = Column(String)
    p_type = Column(String)


class ProposalCreation(Base):
    __tablename__ = 'proposal_creation'

    sl_no = Column(Integer, primary_key=True)
    proposal_id = Column(String)
    financial_year = Column(String, nullable=False)
    project_title = Column(String)
    project_type = Column(String)
    proposal_sub_type = Column(String)
    project_value = Column(Numeric)
    project_technology = Column(String)
    gst_applicable = Column(String)
    status = Column(String)
    step = Column(Integer)
    freeze_flag = Column(String, nullable=False)
    created_by = Column(String, nullable=False)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    consultancy_project_involves = Column(String)
    proposal_to_project_creation_flag = Column(String, nullable=False)
    justification_proposal_involves = Column(String)
    status_remarks = Column(String)
    status_created_by = Column(String)
    status_creation_date = Column(DateTime)
    call_name = Column(String)
    freeze_ts = Column(DateTime)
    forward_remarks = Column(String)
    proposal_com_pk = Column(String)


class ProposalCreationBudgetAllocation(Base):
    __tablename__ = 'proposal_creation_budget_allocation'

    phase = Column(Integer, primary_key=True)
    account_code = Column(Integer, nullable=False)
    budgetted_amount = Column(Float)
    delete_flag = Column(String)
    created_by = Column(String, nullable=False)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    particulars = Column(String)
    proposal_id = Column(String, nullable=False)


class ProposalCreationDept(Base):
    __tablename__ = 'proposal_creation_dept'

    sl_no = Column(Integer, primary_key=True)
    dept = Column(String, nullable=False)
    deptname = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    modified_by = Column(String)
    modification_date = Column(String)
    proposal_id = Column(String, nullable=False)
    appv_status = Column(String, nullable=False)
    appv_remarks = Column(String)
    approved_by = Column(String)
    approval_time = Column(DateTime)


class ProposalCreationInvestigator(Base):
    __tablename__ = 'proposal_creation_investigator'

    sl_no = Column(Integer, primary_key=True)
    stake_code = Column(String, nullable=False)
    stake_type = Column(String)
    stake_dept = Column(String)
    investigator_type = Column(String, nullable=False)
    stake_name = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    proposal_id = Column(String, nullable=False)
    remarks = Column(String)


class ProposalCreationSponsor(Base):
    __tablename__ = 'proposal_creation_sponsor'

    sl_no = Column(Integer, primary_key=True)
    sponsor_code = Column(String, nullable=False)
    sponsor_name = Column(String)
    sponsor_addr = Column(String)
    sponsor_contact_person = Column(String)
    sponsor_contact_no = Column(String)
    sponsor_email = Column(String)
    sponsor_remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    sponsor_type = Column(String)
    fax_no = Column(String)
    sponsor_web_site = Column(String)
    proposal_id = Column(String, nullable=False)


class ProposalCreationStaffDetails(Base):
    __tablename__ = 'proposal_creation_staff_details'

    sl_no = Column(Integer, primary_key=True)
    post_name = Column(String, nullable=False)
    compensation_per_head_month = Column(Numeric)
    no_of_post = Column(Integer)
    total_compensation_per_month = Column(Numeric)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    post_code = Column(String)
    duration = Column(Integer)
    hra = Column(String)
    proposal_id = Column(String, nullable=False)
    modification_date = Column(DateTime)
    modify_by = Column(String)


class ProposalProjDocs(Base):
    __tablename__ = 'proposal_proj_docs'

    prop_proj_code = Column(String, primary_key=True)
    slno = Column(Integer, nullable=False)
    title = Column(String)
    doc_id = Column(String)
    doc_type = Column(String)
    doc_date = Column(Date)
    created_by = Column(String)
    creation_time = Column(DateTime)
    file_ext = Column(String)


class ProposalStaffSanctionedDetails(Base):
    __tablename__ = 'proposal_staff_sanctioned_details'

    designation = Column(String, primary_key=True)
    consolidated_compensation = Column(Float)
    no_of_post = Column(Numeric)
    remarks = Column(String)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    proposal_user_code = Column(String, nullable=False)
    proposal_version = Column(Float, nullable=False)


class ProposedBudgetAllocation(Base):
    __tablename__ = 'proposed_budget_allocation'

    phase = Column(Integer, primary_key=True)
    account_code = Column(Integer, nullable=False)
    budgetted_amount = Column(Float)
    delete_flag = Column(String)
    created_by = Column(String, nullable=False)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    particulars = Column(String)
    proposal_id = Column(String, nullable=False)


class ProposedInvestigator(Base):
    __tablename__ = 'proposed_investigator'

    sl_no = Column(Integer, primary_key=True)
    stake_code = Column(String, nullable=False)
    stake_type = Column(String)
    stake_dept = Column(String)
    investigator_type = Column(String, nullable=False)
    stake_name = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    proposal_id = Column(String, nullable=False)
    remarks = Column(String)


class ProposedMilestone(Base):
    __tablename__ = 'proposed_milestone'

    proposal_code = Column(String, primary_key=True)
    proposed_int_code = Column(Integer, nullable=False)
    milestone = Column(Integer, nullable=False)
    proj_code = Column(String)
    expected_end_date = Column(Date)
    from_month = Column(Integer)
    to_month = Column(Integer)
    milestone_description = Column(String)
    created_by = Column(String)
    creation_time = Column(String)


class ProposedProjStaffDetails(Base):
    __tablename__ = 'proposed_proj_staff_details'

    sl_no = Column(Integer, primary_key=True)
    post_name = Column(String, nullable=False)
    compensation_per_head_month = Column(Numeric)
    no_of_post = Column(Integer)
    total_compensation_per_month = Column(Numeric)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    post_code = Column(String)
    duration = Column(Integer)
    hra = Column(String)
    proposal_id = Column(String, nullable=False)
    modification_date = Column(DateTime)
    modify_by = Column(String)


class ProposedSponsor(Base):
    __tablename__ = 'proposed_sponsor'

    sl_no = Column(Integer, primary_key=True)
    sponsor_code = Column(String, nullable=False)
    sponsor_name = Column(String)
    sponsor_addr = Column(String)
    sponsor_contact_person = Column(String)
    sponsor_contact_no = Column(String)
    sponsor_email = Column(String)
    sponsor_remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    sponsor_type = Column(String)
    fax_no = Column(String)
    sponsor_web_site = Column(String)
    proposal_id = Column(String, nullable=False)


class ProposedTermsOfPayments(Base):
    __tablename__ = 'proposed_terms_of_payments'

    proposal_code = Column(String, primary_key=True)
    proposal_int_code = Column(Integer, nullable=False)
    slno = Column(Integer, nullable=False)
    condition = Column(String)
    description = Column(String)
    period_from_str_date_in_months = Column(Integer)
    period_to_str_date_in_months = Column(Integer)
    percentage_of_payment = Column(Integer)
    amount = Column(Float)


class ProvisionalOfferList(Base):
    __tablename__ = 'provisional_offer_list'

    applicant_name = Column(String)
    email = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    project_code = Column(Integer, primary_key=True)
    order_no = Column(String)
    order_date = Column(Date)
    designation = Column(String)
    dept = Column(String)
    guide = Column(String)
    last_date = Column(Date)
    fellowship_amount = Column(Numeric)
    created_by = Column(String)
    creation_date = Column(DateTime)
    mail_date = Column(DateTime)
    appl_no = Column(String)
    send_mail = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    esex = Column(String)
    send_mail_date = Column(DateTime)
    file_full_path = Column(String)
    phone_no = Column(String)


class PtaxRate(Base):
    __tablename__ = 'ptax_rate'

    sl_no = Column(Integer, primary_key=True)
    min_sal = Column(Numeric, nullable=False)
    max_sal = Column(Numeric, nullable=False)
    rate = Column(Numeric)
    delete_flag = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)


class ReceiptDemand(Base):
    __tablename__ = 'receipt_demand'

    financial_year = Column(String, nullable=False)
    project_code = Column(Integer, primary_key=True)
    demand_no = Column(String, nullable=False)
    pi_copi = Column(String)
    receipt_amount = Column(Numeric)
    receipt_date = Column(DateTime)
    purpose = Column(String)
    status = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    dept = Column(String)
    freeze_by = Column(String)
    freeze_ts = Column(DateTime)
    hardcopy_accepted_date = Column(DateTime)


class ReceiptDemandDetails(Base):
    __tablename__ = 'receipt_demand_details'

    financial_year = Column(String, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    demand_no = Column(String, nullable=False)
    customer_name = Column(String)
    customer_address = Column(String)
    gstin = Column(String)
    state = Column(String)
    country = Column(String)
    email_id = Column(String)
    cheque_dd_no = Column(String)
    chque_dd_date = Column(Date)
    amount = Column(Numeric)
    remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    drawn_on = Column(String)
    in_favour_of = Column(String)
    contact_no = Column(String)
    inv_no = Column(String)
    inv_generation_date = Column(DateTime)
    inv_flag = Column(String, nullable=False)
    letter_ref_no = Column(String)
    receipt_no = Column(Integer)
    receipt_date = Column(DateTime)
    receipt_financial_year = Column(String)
    receipt_status = Column(String, nullable=False)


class RecommendationApproval(Base):
    __tablename__ = 'recommendation_approval'

    serial_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    adv_serial_no = Column(Integer, nullable=False)
    ref_no = Column(String, nullable=False)
    status = Column(String, nullable=False)
    remarks = Column(String)
    creation_time = Column(DateTime)
    created_by = Column(String)


class Recruitment(Base):
    __tablename__ = 'recruitment'

    serial_no = Column(String, primary_key=True)
    walkin_flag = Column(String)
    designation = Column(String)
    post = Column(String)
    qual_exp = Column(String)
    salary_from = Column(String)
    salary_to = Column(String)
    relevant_exp = Column(String)
    age_limit = Column(String)
    tenure = Column(String)
    ref_no = Column(String)
    project_code = Column(Integer)
    adv_serial_no = Column(Integer)
    pi_app_flag = Column(String)
    sric_flag = Column(String)
    hod_flag = Column(String)
    dean_flag = Column(String)
    board_request_flag = Column(String)
    hod_int_flag = Column(String)
    dean_int_flag = Column(String)
    board_form_flag = Column(String)
    first_date = Column(Date)
    last_date = Column(Date)
    walkin_date = Column(Date)
    int_hr = Column(String)
    int_min = Column(String)
    int_mer = Column(String)
    venue = Column(String)
    shtcr = Column(Text)
    sric_comment = Column(String)
    hod_comment = Column(String)
    dean_comment = Column(String)
    hod_int_comment = Column(String)
    dean_int_comment = Column(String)
    sric_int_comment = Column(String)
    success_flag = Column(String)
    all_complete_flag = Column(String)
    select_flag = Column(String)
    round_no = Column(Integer)
    brd_round_no = Column(Integer)
    fee = Column(String)
    joining_date = Column(Date)
    dean_st_approval = Column(String)
    sric_app_time = Column(DateTime)
    sric_brd_app_time = Column(DateTime)
    edited_by = Column(String)
    spl_walkin = Column(String)
    dept = Column(String)
    pi = Column(String)
    forwarded_by = Column(String)
    pi_req_time = Column(DateTime)
    dean_app_time = Column(DateTime)
    head_app_time = Column(DateTime)
    edit_time = Column(DateTime)
    pi_brd_req_by = Column(String)
    pi_brd_req_time = Column(DateTime)
    head_brd_req_by = Column(String)
    head_brd_req_time = Column(DateTime)
    dean_brd_req_by = Column(String)
    dean_brd_req_time = Column(DateTime)
    sric_brd_req_by = Column(String)
    sric_brd_req_time = Column(DateTime)
    head_app_code = Column(String)
    head_brd_code = Column(String)
    sric_app_by = Column(String)
    dean_app_by = Column(String)
    more_information = Column(String)
    remarks = Column(String)
    adv_close_flag = Column(String)
    close_date = Column(DateTime)
    close_remarks = Column(String)
    status_changed_by = Column(String)
    specialization_sl_no = Column(Integer)
    level_pay_matrix = Column(String)
    adv_type = Column(String)
    apply_link = Column(String)
    efile_id = Column(String)
    efile_ts = Column(DateTime)
    efile_gen_by = Column(String)
    enote_id = Column(String)
    oth_remarks = Column(String)
    new_project_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    project_title = Column(String)
    sponsor_letter_no = Column(String)
    sponsor_letter_date = Column(Date)
    sponsor_name_address = Column(String)
    supporting_file_id = Column(String)
    female_application_fees = Column(Numeric, nullable=False)
    sc_st_application_fees = Column(Numeric, nullable=False)
    others_desg = Column(String)
    delete_flag = Column(String, nullable=False)


class RecruitmentBoard(Base):
    __tablename__ = 'recruitment_board'

    emp_code = Column(String, nullable=False)
    is_emp_flag = Column(String)
    creation_time = Column(DateTime)
    emp_desg = Column(String)
    member_sl_no = Column(Integer, nullable=False)
    emp_email = Column(String)
    adv_serial_no = Column(Integer, nullable=False)
    project_code = Column(Integer, primary_key=True)
    recommended = Column(String, nullable=False)
    recommended_date = Column(DateTime)
    recommended_remarks = Column(String)
    recommended_by = Column(String)


class RequestForAdvanceAdjustment(Base):
    __tablename__ = 'request_for_advance_adjustment'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    request_id = Column(String)
    advance_bill_no = Column(String)
    adjustment_bill_no = Column(String)
    acc_head = Column(Integer)
    remarks = Column(String)
    adjustment_amount = Column(Numeric)
    refund_amount = Column(Numeric)
    refund_id = Column(String)
    status = Column(String)
    fund_booking_no = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    e_office_no = Column(String)
    e_office_date = Column(Date)


class RequestForAdvanceAdjustmentHistory(Base):
    __tablename__ = 'request_for_advance_adjustment_history'

    h_sl_no = Column(Integer, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    financial_year = Column(String, nullable=False)
    request_id = Column(String)
    advance_bill_no = Column(String)
    adjustment_bill_no = Column(String)
    acc_head = Column(Integer)
    remarks = Column(String)
    adjustment_amount = Column(Numeric)
    refund_amount = Column(Numeric)
    refund_id = Column(String)
    status = Column(String)
    fund_booking_no = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    e_office_no = Column(String)
    e_office_date = Column(Date)


class RequestForNewBankAccount(Base):
    __tablename__ = 'request_for_new_bank_account'

    sl_no = Column(Integer, primary_key=True)
    sric_id = Column(String, nullable=False)
    project_code = Column(Integer)
    bank_name = Column(String)
    bank_address = Column(String)
    ifsc = Column(String)
    account_no = Column(String)
    pan_no = Column(String)
    account_type = Column(String)
    remarks = Column(String)
    status = Column(String)
    account_file = Column(LargeBinary)
    pan_file = Column(LargeBinary)
    sric_remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    aadhaar_no = Column(String)


class RequestForPayment(Base):
    __tablename__ = 'request_for_payment'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String, nullable=False)
    project_code = Column(Integer, nullable=False)
    token_id = Column(String)
    amount = Column(Numeric)
    appv_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String)
    pi = Column(String)
    pi_appv_date = Column(DateTime)
    sao_ar_remarks = Column(String)
    dean_remarks = Column(String)


class RequestForPaymentDetails(Base):
    __tablename__ = 'request_for_payment_details'

    sl_no = Column(Integer, primary_key=True)
    token_id = Column(String, nullable=False)
    particulars = Column(String)
    sub_vch_no = Column(String)
    amount = Column(Numeric)
    remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String)
    head_of_expenditure = Column(String)
    payee_name = Column(String)
    ref_sl_no = Column(Integer)


class RoleMenuDetail(Base):
    __tablename__ = 'role_menu_detail'

    role_code = Column(String, primary_key=True)
    menu_id = Column(Numeric, nullable=False)
    activated_from = Column(Date, nullable=False)
    activated_to = Column(Date)
    access_status = Column(String, nullable=False)
    activated_by = Column(String)
    activation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    create_flag = Column(String)
    read_flag = Column(String)
    update_flag = Column(String)
    delete_flag = Column(String)


class RoleMenuDetailDept(Base):
    __tablename__ = 'role_menu_detail_dept'

    dept_role_code = Column(String, primary_key=True)
    menu_id = Column(Numeric, nullable=False)
    activated_from = Column(Date, nullable=False)
    activated_to = Column(Date)
    access_status = Column(String, nullable=False)
    activated_by = Column(String)
    activation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    create_flag = Column(String)
    read_flag = Column(String)
    update_flag = Column(String)
    delete_flag = Column(String)


class RoleMenuDetailHistory(Base):
    __tablename__ = 'role_menu_detail_history'

    serial_no = Column(Integer, primary_key=True)
    role_code = Column(String, nullable=False)
    menu_id = Column(Numeric, nullable=False)
    activated_from = Column(Date, nullable=False)
    activated_to = Column(Date)
    access_status = Column(String, nullable=False)
    activated_by = Column(String)
    activation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    create_flag = Column(String)
    read_flag = Column(String)
    update_flag = Column(String)
    delete_flag = Column(String)


class RoleModuleAccess(Base):
    __tablename__ = 'role_module_access'

    role_code = Column(String, primary_key=True)
    module_code = Column(Numeric, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)


class RuntimeExceptionMaster(Base):
    __tablename__ = 'runtime_exception_master'

    sl_no = Column(Integer, primary_key=True)
    err_user = Column(String)
    err_date = Column(DateTime)
    err_loc = Column(String)
    err_msg = Column(String)
    remarks = Column(String)


class SalaryDetails(Base):
    __tablename__ = 'salary_details'

    empno = Column(String, nullable=False)
    yr = Column(String, nullable=False)
    mon = Column(String, nullable=False)
    project_code = Column(Integer, primary_key=True)
    acc_no = Column(String)
    bill_no = Column(String)
    cash_book = Column(String)
    net_sal = Column(Numeric)
    arrear = Column(Numeric)
    gross = Column(Numeric)
    ptax = Column(Numeric)
    itax = Column(Numeric)
    vsrc = Column(Numeric)
    lfees = Column(Numeric)
    electric = Column(Numeric)
    misc = Column(Numeric)
    remarks = Column(String)
    delete_flag = Column(String)
    created_by = Column(String)
    creation_dt = Column(DateTime, nullable=False)
    modify_by = Column(String)
    modify_dt = Column(DateTime)
    status = Column(String)
    emp_type = Column(String)
    file_full_path = Column(String)
    ppf = Column(Numeric)
    hra = Column(Numeric)
    online_flag = Column(String, nullable=False)
    demand_no = Column(String)
    refund_hra_amount = Column(Numeric)
    booking_id = Column(String)
    monthly_cashbook_run_count = Column(Integer)
    hmc_charges = Column(Numeric)
    onrole_student = Column(String, nullable=False)


class SalaryVsrcRoomRentAllocation(Base):
    __tablename__ = 'salary_vsrc_room_rent_allocation'

    sric_id = Column(String, nullable=False)
    vsrc_id = Column(String, nullable=False)
    yr = Column(Integer, nullable=False)
    mon = Column(Integer, nullable=False)
    block = Column(String, nullable=False)
    room_no = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    room_rent = Column(Numeric, nullable=False)
    remarks = Column(String)
    status = Column(String, nullable=False)
    recov_yr = Column(Integer)
    recov_mon = Column(Integer)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    sric_remarks = Column(String)
    demand_no = Column(String)
    allotment_from_date = Column(Date)
    allotment_to_date = Column(Date)
    bed_no = Column(String, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    water_charge = Column(Numeric, nullable=False)
    electric_charge = Column(Numeric, nullable=False)
    hmc_charges = Column(Numeric)
    onrole_student = Column(String, nullable=False)
    hallcode = Column(String)


class ScheemMaster(Base):
    __tablename__ = 'scheem_master'

    serial_no = Column(Integer, primary_key=True)
    scheem_code = Column(String, nullable=False)
    scheem_description = Column(String)
    delete_flag = Column(String)


class SchemAccountMappingTab(Base):
    __tablename__ = 'schem_account_mapping_tab'

    scheme_code = Column(String, nullable=False)
    project_code = Column(String, primary_key=True)
    account_no = Column(String, nullable=False)
    mapped_by = Column(String)
    mapping_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    comp_code = Column(String, nullable=False)
    delete_flag = Column(String)
    final_flag = Column(String)


class ServiceContractFundBooking(Base):
    __tablename__ = 'service_contract_fund_booking'

    application_no = Column(String, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    office_order_no = Column(String, nullable=False)
    office_order_date = Column(Date)
    from_date = Column(Date)
    to_date = Column(Date)
    amount = Column(Numeric)
    freeze_flag = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    tenure_remarks = Column(String)
    ledger_flag = Column(String)


class ServiceContractLedger(Base):
    __tablename__ = 'service_contract_ledger'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    application_id = Column(String, nullable=False)
    order_id = Column(String, nullable=False)
    no_of_days = Column(Integer)
    balance_date = Column(Date)
    op_bal = Column(Numeric)
    receipt_amount = Column(Numeric)
    payment_amount = Column(Numeric)
    cl_bal = Column(Numeric)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    in_process_amount = Column(Numeric)
    in_process_day = Column(Integer)


class ServiceContractSalary(Base):
    __tablename__ = 'service_contract_salary'

    sl_no = Column(Integer, primary_key=True)
    project_code = Column(Integer, nullable=False)
    order_id = Column(String, nullable=False)
    staff_id = Column(String, nullable=False)
    from_dt = Column(Date)
    to_dt = Column(Date)
    amount = Column(Numeric)
    remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    status_flag = Column(String)
    tax_val = Column(Numeric)
    ot_deduct = Column(Numeric)
    ot_reason = Column(String)
    bill_no = Column(String)
    tax_coa = Column(Integer)
    booking_id = Column(String)
    vsrc_oth_deduct = Column(Numeric)
    vsrc_oth_deduct_coa = Column(String)
    vsrc_oth_deduct_remarks = Column(String)
    electric_fee = Column(Numeric)
    electric_fee_coa = Column(String)


class SponsorMaster(Base):
    __tablename__ = 'sponsor_master'

    sponsor_code = Column(Integer, primary_key=True)
    sponsor_name = Column(String, nullable=False)
    sponsor_type = Column(String)
    full_address = Column(String)
    remarks = Column(String)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    contact_no = Column(String)
    e_mail = Column(String)
    description = Column(String)
    group_sponsor_code = Column(Integer)
    country = Column(String)
    inst_vendor_code = Column(String)
    gstin = Column(String)
    city = Column(String)
    state = Column(String)
    composite_scheme = Column(String)
    pan_no = Column(String)
    tan_no = Column(String)
    pin = Column(String)
    street_name = Column(String)
    room_no = Column(String)
    floor = Column(String)
    city_village_town = Column(String)
    district = Column(String)


class SponsorTypeMaster(Base):
    __tablename__ = 'sponsor_type_master'

    type_code = Column(String, primary_key=True)
    type_desc = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    sponsor_type = Column(String)
    sponsor_belongs_to = Column(String)


class SricBillOfSupply(Base):
    __tablename__ = 'sric_bill_of_supply'

    sl_no = Column(Integer, primary_key=True)
    financial_year = Column(String)
    org_id = Column(String)
    project_id = Column(Integer)
    invoice_date = Column(Date)
    invoice_no = Column(String)
    supplier_id = Column(String)
    hsn_sac = Column(String)
    bill_amount = Column(Numeric)
    customer_id = Column(String)
    customer_name = Column(String)
    consignee_id = Column(String)
    consignee_name = Column(String)
    supply_date = Column(DateTime)
    supply_state = Column(String)
    goods_or_service = Column(String)
    status = Column(String)
    remarks = Column(String)
    actual_invoice_id = Column(String)
    bos_mst_com_pk = Column(String)
    reference_id = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    delete_flag = Column(String)
    reverse_charges = Column(String)
    uom = Column(String)
    qty = Column(Integer)
    description = Column(String)
    bos_year = Column(String)


class SricDocMaster(Base):
    __tablename__ = 'sric_doc_master'

    process_id = Column(String, primary_key=True)
    doc_name = Column(String, nullable=False)
    doc_path = Column(String, nullable=False)
    doc_type = Column(String)
    doc = Column(LargeBinary)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    delete_flag = Column(String, nullable=False)
    remarks = Column(String)


class SricDocRepo(Base):
    __tablename__ = 'sric_doc_repo'

    project_file_type = Column(String, nullable=False)
    file = Column(LargeBinary)
    file_ext_type = Column(String)
    entry_by = Column(String)
    entry_ts = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    proposal_id = Column(String, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    remarks = Column(String)


class SricDpcode(Base):
    __tablename__ = 'sric_dpcode'

    dept = Column(String, primary_key=True)
    depname = Column(String, nullable=False)
    deptype = Column(String)
    depsubtype = Column(String)
    type_order = Column(Integer)


class SricEmpmas(Base):
    __tablename__ = 'sric_empmas'

    empno = Column(String, primary_key=True)
    empname = Column(String)
    present_designation = Column(String)
    present_department = Column(String)
    emptype = Column(String)
    date_of_birth = Column(Date)
    date_of_initial_join = Column(Date)
    date_of_persent_expiration = Column(Date)
    present_add = Column(String)
    permanent_add = Column(String)
    in_service = Column(String)
    guidance_flag = Column(String)


class SricFdfTest(Base):
    __tablename__ = 'sric_fdf_test'

    sl_no = Column(Integer, primary_key=True)
    fin_year = Column(String)
    dept_code = Column(String)
    empname = Column(String)
    opening_balance = Column(String)
    receipt_amt = Column(String)
    payment_amt = Column(String)
    closing_balance = Column(String)
    empno = Column(String)
    possible_empno = Column(String)


class SricProjectInchargeDetails(Base):
    __tablename__ = 'sric_project_incharge_details'

    user_project_code = Column(String, primary_key=True)
    type = Column(String)
    stakeholder_name = Column(String)
    stakeholder_type = Column(String)
    stakeholder_dept = Column(String)
    stakeholder_code = Column(String)


class SricProjectMaster(Base):
    __tablename__ = 'sric_project_master'

    project_type = Column(String)
    project_code = Column(Integer, primary_key=True)
    user_project_code = Column(String)
    title = Column(String)
    total_sanctioned_grant = Column(Numeric)
    date_of_commencement = Column(Date)
    closing_date = Column(Date)
    sric_cl_flg = Column(String)
    delete_flag = Column(String)
    sric_virtual_project_flag = Column(String)


class SricProjectStaffMaster(Base):
    __tablename__ = 'sric_project_staff_master'

    empno = Column(String, primary_key=True)
    empname = Column(String)
    emp_sex = Column(String)
    emp_maritalsts = Column(String)
    empbasic = Column(String)
    emp_lastbasic = Column(String)
    date_of_birth = Column(Date)
    date_of_initial_join = Column(Date)
    date_of_persent_expiration = Column(Date)
    empdesg = Column(String)
    empdept = Column(String)
    in_service = Column(String)
    pan_no = Column(String)
    account_no = Column(String)
    date_of_persent_leaving = Column(Date)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    project_code = Column(String)
    delete_flag = Column(String)
    roll_no = Column(String)
    joining_confirmation = Column(String)
    stake_holder_type = Column(Text)
    user_project_code = Column(String)


class SricResearchCouncil(Base):
    __tablename__ = 'sric_research_council'

    research_id = Column(String, primary_key=True)
    research_description = Column(String, nullable=False)
    delete_flag = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modify_by = Column(String)
    modified_date = Column(String)


class StaffSalaryFellowshipClaim(Base):
    __tablename__ = 'staff_salary_fellowship_claim'

    sl_no = Column(Integer, primary_key=True)
    yr = Column(String, nullable=False)
    mnth = Column(String, nullable=False)
    no_of_days = Column(Integer)
    attendance = Column(Integer)
    project_code = Column(Integer, nullable=False)
    sric_id = Column(String, nullable=False)
    remarks = Column(String)
    amount = Column(Numeric)
    arrear_amount = Column(Numeric)
    status = Column(String)
    ref_no = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modified_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    booking_id = Column(String)


class StaffSalaryFellowshipClaimHistory(Base):
    __tablename__ = 'staff_salary_fellowship_claim_history'

    hist_sl_no = Column(Integer, nullable=False)
    sl_no = Column(Integer, primary_key=True)
    yr = Column(String, nullable=False)
    mnth = Column(String, nullable=False)
    no_of_days = Column(Integer)
    attendance = Column(Integer)
    project_code = Column(Integer, nullable=False)
    sric_id = Column(String, nullable=False)
    remarks = Column(String)
    amount = Column(Numeric)
    arrear_amount = Column(Numeric)
    status = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    booking_id = Column(String)


class StakeholderDetails(Base):
    __tablename__ = 'stakeholder_details'

    stakeholder_code = Column(String, primary_key=True)
    stakeholder_name = Column(String)
    stakeholder_dept = Column(String)
    stakeholder_type = Column(String)
    onrole_flag = Column(String)


class StakeholderDetailsFdw(Base):
    __tablename__ = 'stakeholder_details_fdw'

    stakeholder_code = Column(String, primary_key=True)
    stakeholder_name = Column(String)
    stakeholder_dept = Column(String)
    stakeholder_type = Column(String)
    onrole_flag = Column(String)


class StudentmasPg(Base):
    __tablename__ = 'studentmas_pg'

    rollno = Column(String, primary_key=True)
    name = Column(String)
    specialisation = Column(String)
    dept = Column(String)
    hall = Column(String)
    sex = Column(String)
    category = Column(String)
    father_name = Column(String)
    guardian_name = Column(String)
    date_of_birth = Column(DateTime)
    fat_guard_mincome = Column(String)
    parental_profession = Column(String)
    mail_houseno = Column(String)
    mail_street = Column(String)
    mail_city = Column(String)
    mail_state = Column(String)
    mail_country = Column(String)
    mail_zipno = Column(String)
    per_houseno = Column(String)
    per_street = Column(String)
    per_city = Column(String)
    per_state = Column(String)
    per_country = Column(String)
    per_zipno = Column(String)
    phone_no = Column(String)
    nationality = Column(String)
    native_state = Column(String)
    mother_tongue = Column(String)
    passport_no = Column(String)
    blood_group = Column(String)
    height = Column(String)
    weight = Column(String)
    qualify_exam_name = Column(String)
    qualify_exam_year = Column(String)
    qualify_exam_class = Column(String)
    percent_marks_gpa = Column(String)
    board_or_univ = Column(String)
    graduation = Column(String)
    join_flag = Column(String)
    nature_of_admission = Column(String)
    email_add = Column(String)
    year_of_admiss = Column(String)
    degree_type = Column(String)
    gate_regn_no = Column(String)
    gate_branch = Column(String)
    gate_percentile = Column(String)
    all_india_rank = Column(String)
    current_place_stay = Column(String)
    country = Column(String)
    bank_acc_no = Column(String)
    scholar_category = Column(String)
    schol_name = Column(String)
    schol_amount = Column(String)
    idcardno = Column(String)
    idmark = Column(String)
    police_station = Column(String)
    mtech_regno = Column(String)
    amount_paid = Column(String)
    room = Column(String)
    gate_score = Column(String)
    course_completed = Column(String)
    photo_image_path = Column(String)
    sign_image_path = Column(String)
    photo_image_name = Column(String)
    sign_image_name = Column(String)
    year_of_passing = Column(String)


class TaDaMaster(Base):
    __tablename__ = 'ta_da_master'

    org_id = Column(String, nullable=False)
    payee_id = Column(String, nullable=False)
    slno = Column(Integer, nullable=False)
    journey_desc = Column(String)
    ref_no = Column(String)
    status = Column(String)
    ta_da_master_com_pk = Column(String, nullable=False)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    pda_mst_com_pk = Column(String)
    project_id = Column(String)
    cost_center_id = Column(String)
    final_submitted_on = Column(DateTime)
    project_code = Column(Integer, primary_key=True)
    appv_type = Column(String)
    fin_yr = Column(String, nullable=False)
    head_id = Column(String)
    temp_user_code = Column(String)


class TaDetails(Base):
    __tablename__ = 'ta_details'

    org_id = Column(String, primary_key=True)
    payee_id = Column(String, nullable=False)
    slno = Column(Integer, nullable=False)
    sub_slno = Column(Integer, nullable=False)
    place_form = Column(String)
    place_from_date = Column(DateTime)
    place_form_time = Column(String)
    place_to = Column(String)
    place_to_date = Column(DateTime)
    place_to_time = Column(String)
    mode_of_journey = Column(String)
    class_of_journey = Column(String)
    distance_in_km = Column(Numeric)
    no_of_fairs = Column(Numeric)
    claimed_amount = Column(Numeric)
    verified_amount = Column(Numeric)
    verification_flag = Column(String)
    ticket_no = Column(String)
    remarks = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    currency_type = Column(String)
    diary_no = Column(String, nullable=False)
    invoice_no = Column(String)
    invoice_date = Column(Date)
    inv_remarks = Column(String)
    inv_file = Column(LargeBinary)
    file_data = Column(LargeBinary)


class TaxStatement(Base):
    __tablename__ = 'tax_statement'

    pan_no = Column(String, nullable=False)
    tax_type = Column(String, nullable=False)
    fin_year = Column(String, primary_key=True)
    slno = Column(Integer, nullable=False)
    quarter = Column(String, nullable=False)
    file_path = Column(String)
    file_name = Column(String)
    uploaded_by = Column(String)
    upload_time = Column(DateTime)


class TdsRate(Base):
    __tablename__ = 'tds_rate'

    financial_year = Column(String, primary_key=True)
    pan_type = Column(String, nullable=False)
    rate = Column(String)
    delete_flag = Column(String)
    type_desc = Column(String)


class TempUser(Base):
    __tablename__ = 'temp_user'

    user_code = Column(String, primary_key=True)
    user_name = Column(String)
    email_id = Column(String, nullable=False)
    from_date = Column(Date)
    to_date = Column(Date)
    otp = Column(String)
    created_by = Column(String)
    creation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(String)
    serial_no = Column(String, nullable=False)


class TermsOfPayments(Base):
    __tablename__ = 'terms_of_payments'

    prop_proj_code = Column(String, primary_key=True)
    slno = Column(Integer, nullable=False)
    condition = Column(String)
    description = Column(String)
    period_from_str_date_in_months = Column(Integer)
    period_to_str_date_in_months = Column(Integer)
    percentage_of_payment = Column(Integer)
    amount = Column(Float)


class TravelDaAllowance(Base):
    __tablename__ = 'travel_da_allowance'

    con_grade_pay_frm = Column(Numeric, primary_key=True)
    con_grade_pay_to = Column(Numeric, nullable=False)
    cond_type = Column(String, nullable=False)
    employment_type = Column(String, nullable=False)
    da_version = Column(String, nullable=False)
    category = Column(String)
    food_chrg = Column(Numeric)
    accom_chrg = Column(Numeric)
    taxi_chrg_city = Column(Numeric)
    taxi_chrg_other = Column(Numeric)
    chrg_unit = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    effected_from = Column(DateTime)


class TravelEntitlement(Base):
    __tablename__ = 'travel_entitlement'

    grade_pay = Column(Integer, primary_key=True)
    scope = Column(String, nullable=False)
    t_mode = Column(String, nullable=False)
    tr_version = Column(String, nullable=False)
    travel_entitlements = Column(String)
    effected_from = Column(DateTime)
    remarks = Column(String)
    amount = Column(Numeric)
    created_by = Column(String)
    creation_time = Column(DateTime)


class UcDoctemplate(Base):
    __tablename__ = 'uc_doctemplate'

    doc_ref_no = Column(String, primary_key=True)
    sponsor = Column(String, nullable=False)
    reference = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)


class UcDocTemplatePageDetails(Base):
    __tablename__ = 'uc_doc_template_page_details'

    sponsor = Column(String, primary_key=True)
    doc_ref_no = Column(String, nullable=False)
    page_no = Column(Integer, nullable=False)
    page_name = Column(String)
    header_include = Column(String)
    content_val = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)


class UcTagMaster(Base):
    __tablename__ = 'uc_tag_master'

    sl_no = Column(Integer, primary_key=True)
    tag_type = Column(String, nullable=False)
    tag_id = Column(String, nullable=False)
    tag_desc = Column(String)
    head_id = Column(Integer)
    phase = Column(Integer)
    query = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)


class UnadjustedAdvanceLoanLedger(Base):
    __tablename__ = 'unadjusted_advance_loan_ledger'

    financial_year = Column(String, nullable=False)
    cash_book = Column(String, nullable=False)
    project_code = Column(String, primary_key=True)
    account_code = Column(String, nullable=False)
    loan_adv_type = Column(String, nullable=False)
    op_balance = Column(Numeric)
    loan_adv_given = Column(Numeric)
    loan_adv_refund = Column(Numeric)
    cl_balance = Column(Numeric)
    status = Column(String, nullable=False)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)


class UserMenuDetail(Base):
    __tablename__ = 'user_menu_detail'

    user_code = Column(String, primary_key=True)
    menu_id = Column(Numeric, nullable=False)
    activated_from = Column(Date, nullable=False)
    activated_to = Column(Date)
    dept_code = Column(String, nullable=False)
    access_status = Column(String, nullable=False)
    activated_by = Column(String)
    activation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    create_flag = Column(String)
    read_flag = Column(String)
    update_flag = Column(String)
    delete_flag = Column(String)
    parent_menu_id = Column(Numeric)
    row_deleted_flag = Column(String)


class UserMenuDetailHistory(Base):
    __tablename__ = 'user_menu_detail_history'

    serial_no = Column(Integer, primary_key=True)
    user_code = Column(String, nullable=False)
    menu_id = Column(Numeric, nullable=False)
    activated_from = Column(Date, nullable=False)
    activated_to = Column(Date)
    dept_code = Column(String, nullable=False)
    access_status = Column(String, nullable=False)
    activated_by = Column(String)
    activation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)
    create_flag = Column(String)
    read_flag = Column(String)
    update_flag = Column(String)
    delete_flag = Column(String)
    parent_menu_id = Column(Numeric)
    row_deleted_flag = Column(String)


class UserModuleAccess(Base):
    __tablename__ = 'user_module_access'

    user_code = Column(String, primary_key=True)
    user_type = Column(String, nullable=False)
    module_code = Column(Numeric, nullable=False)


class UserRoleDetail(Base):
    __tablename__ = 'user_role_detail'

    user_code = Column(String, primary_key=True)
    role_code = Column(String, nullable=False)
    activated_from = Column(Date, nullable=False)
    activated_to = Column(Date, nullable=False)
    dept_code = Column(String, nullable=False)
    access_status = Column(String, nullable=False)
    activated_by = Column(String)
    activation_date = Column(Date)
    modified_by = Column(String)
    modification_date = Column(Date)


class VendorBillDetails(Base):
    __tablename__ = 'vendor_bill_details'

    sl_no = Column(Integer, primary_key=True)
    fin_yr = Column(String, nullable=False)
    project_code = Column(Integer)
    chart_of_account = Column(String)
    payee_code = Column(String)
    claim_amount = Column(Numeric)
    bill_owner_name = Column(String)
    bill_owner_code = Column(String)
    actual_paid_amt = Column(Numeric)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modify_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String)
    approval_flag = Column(String)
    approval_dt = Column(DateTime)
    receipt_no = Column(Integer)
    acc_no = Column(String)
    acq_roll = Column(String)
    user_type = Column(String)
    ref_no = Column(String)
    remarks1 = Column(String)
    remarks2 = Column(String)
    gh_demand_no = Column(String)


class ViwAccVendorMaster(Base):
    __tablename__ = 'viw_acc_vendor_master'

    vendor_code = Column(String, primary_key=True)
    vendor_name = Column(String)
    vendor_address = Column(String)
    pan_no = Column(String)
    bank_ac_no = Column(String)
    bank_code = Column(String)
    bank_address = Column(String)
    active_flag = Column(String)
    vat_no = Column(String)
    cst_no = Column(String)
    holding_premise = Column(String)
    street_name = Column(String)
    room_no = Column(String)
    floor = Column(String)
    city_village_town = Column(String)
    district = Column(String)
    state = Column(String)
    country = Column(String)
    pin = Column(String)
    e_mail = Column(String)
    contact_no = Column(String)
    swift_code = Column(String)
    ibn_no = Column(String)
    service_tax_no = Column(String)


class ViwAdmissionChannelMst(Base):
    __tablename__ = 'viw_admission_channel_mst'

    admit_exam = Column(String, primary_key=True)
    stu_type = Column(String)
    category = Column(String)
    subcategory = Column(String)


class ViwAdmRoleMaster(Base):
    __tablename__ = 'viw_adm_role_master'

    role_code = Column(String, primary_key=True)
    role_description = Column(String)
    statutory_flag = Column(String)
    secretary_to_whom = Column(String)
    dept_code = Column(String)
    function_code = Column(String)


class ViwAttachmentMaster(Base):
    __tablename__ = 'viw_attachment_master'

    attachment_code = Column(String, primary_key=True)
    attachment_desc = Column(String)


class ViwAuthorityMaster(Base):
    __tablename__ = 'viw_authority_master'

    authority_type = Column(String, primary_key=True)
    authority_for = Column(String)
    authority_for_data_type = Column(String)
    authority_code = Column(String)
    authority_code_data_type = Column(String)
    active_from = Column(String)
    active_to = Column(String)
    created_by = Column(String)
    creation_time = Column(String)
    modified_by = Column(String)
    modification_time = Column(String)


class ViwComAddr(Base):
    __tablename__ = 'viw_com_addr'

    stake_holder_code = Column(String, primary_key=True)
    stake_holder_type = Column(String)
    addr_type = Column(String)
    addr = Column(String)
    vill_town_city = Column(String)
    police_station = Column(String)
    pin = Column(String)
    district = Column(String)
    state = Column(String)
    country = Column(String)


class ViwComContact(Base):
    __tablename__ = 'viw_com_contact'

    stake_holder_code = Column(String, primary_key=True)
    stake_holder_type = Column(String)
    contact_type = Column(String)
    contact_type_val = Column(String)


class ViwCountryList(Base):
    __tablename__ = 'viw_country_list'

    sl_no = Column(Integer, primary_key=True)
    country_name = Column(String)


class ViwCountryMst(Base):
    __tablename__ = 'viw_country_mst'

    country_code = Column(String, primary_key=True)
    country_name = Column(String)
    country_isd = Column(String)


class ViwCrfEquipment(Base):
    __tablename__ = 'viw_crf_equipment'

    project_code = Column(String, primary_key=True)
    project_code_ext = Column(String)
    lab_division = Column(String)
    crf_lab_id = Column(String)
    crf_lab_name = Column(String)
    crf_lab_pi = Column(String)
    crf_lab_co_pi = Column(String)
    inst_charge = Column(String)
    project_charge = Column(String)
    oth_acad_inst_charge = Column(String)
    res_dev_charge = Column(String)
    gst_value = Column(String)
    overhead = Column(String)
    lab_slot_def = Column(String)
    measuring_unit = Column(String)
    measuring_unit_remarks = Column(String)
    tarrif_det = Column(String)
    working_status = Column(String)
    deptcode = Column(String)


class ViwCrfLabSlotBooking(Base):
    __tablename__ = 'viw_crf_lab_slot_booking'

    crf_lab_id = Column(String, primary_key=True)
    slno = Column(String)
    reference_id = Column(String)
    book_fee_amount = Column(String)
    book_fee_paid = Column(String)
    book_fee_paid_by = Column(String)
    book_fee_paid_on = Column(String)
    budget_allocation_id = Column(String)
    fee_reference_id = Column(String)
    book_fee_rem = Column(String)
    booked_project_code = Column(String)


class ViwDeptRoleMaster(Base):
    __tablename__ = 'viw_dept_role_master'

    role_code = Column(String, primary_key=True)
    role_type = Column(String)
    role_description = Column(String)
    local = Column(String)
    parent_role_code = Column(String)
    active_flag = Column(String)


class ViwDgcode(Base):
    __tablename__ = 'viw_dgcode'

    code = Column(String, primary_key=True)
    long = Column(String)


class ViwDpcode(Base):
    __tablename__ = 'viw_dpcode'

    dept = Column(String, primary_key=True)
    depname = Column(String)
    deptype = Column(String)
    depsubtype = Column(String)


class ViwEmpmas(Base):
    __tablename__ = 'viw_empmas'

    empno = Column(String, primary_key=True)
    empname = Column(String)
    emp_sex = Column(String)
    emp_maritalsts = Column(String)
    emp_father = Column(String)
    emp_prsadd = Column(String)
    emp_pmtadd = Column(String)
    emp_edu = Column(String)
    emp_pedu = Column(String)
    emp_cast = Column(String)
    blood_group = Column(String)
    empbasic = Column(String)
    emp_lastbasic = Column(String)
    empdob = Column(String)
    empdoj = Column(String)
    time_join = Column(String)
    empdni = Column(String)
    empdor = Column(String)
    empdesg = Column(String)
    empsubpst = Column(String)
    emp_inidesgn = Column(String)
    empdept = Column(String)
    empclas = Column(String)
    place_of_posting = Column(String)
    hra_flag = Column(String)
    npa_flag = Column(String)
    handy_flag = Column(String)
    empstatus = Column(String)
    eol_status = Column(String)
    on_deputation = Column(String)
    salcode = Column(String)
    salsrno = Column(String)
    empbankac = Column(String)
    pay_yn = Column(String)
    pftype = Column(String)
    scale_ind = Column(String)
    eb_flag = Column(String)
    punish_flag = Column(String)
    on_prob = Column(String)
    con_dt = Column(String)
    prob_prd = Column(String)
    promot_dt = Column(String)
    elcrdt = Column(String)
    hplcrdt = Column(String)
    emplstincdt = Column(String)
    vactype = Column(String)
    lastpromodt = Column(String)
    dt_reg_exp = Column(String)
    oo_no_dt = Column(String)
    appt_type = Column(String)
    sal_status = Column(String)
    religion = Column(String)
    last_prom_dt = Column(String)
    place_birth = Column(String)
    in_service = Column(String)
    file_no = Column(String)
    specialisation1 = Column(String)
    specialisation2 = Column(String)
    pan_no = Column(String)
    bank_code = Column(String)


class ViwEstateHouseMonthlyLfeeEc(Base):
    __tablename__ = 'viw_estate_house_monthly_lfee_ec'

    yr = Column(Integer, primary_key=True)
    mnth = Column(Integer)
    empno = Column(String)
    wc_arrear = Column(Numeric)
    wc_refund = Column(Numeric)
    wc = Column(Numeric)
    twc = Column(Numeric)
    cr_arrear = Column(Numeric)
    cr_refund = Column(Numeric)
    cr = Column(Numeric)
    tcr = Column(Numeric)
    lfeemsg = Column(String)
    lfee_computation_flag = Column(String)
    lfee_computed_by = Column(String)
    lfee_computation_time = Column(DateTime)
    ec_arrear = Column(Numeric)
    ec_refund = Column(Numeric)
    phase_unit = Column(Integer)
    ec = Column(Numeric)
    mtr_rent = Column(Numeric)
    tec = Column(Numeric)
    fsc = Column(Numeric)
    tec1 = Column(Numeric)
    eduty = Column(Numeric)
    tec2 = Column(Numeric)
    netec = Column(Numeric)
    ecmsg = Column(String)
    ec_computation_flag = Column(String)
    ec_computed_by = Column(String)
    ec_computation_time = Column(DateTime)
    paid_flag = Column(String)
    paid_flag_updated_by = Column(String)
    paid_flag_updation_time = Column(DateTime)
    payment_mode = Column(String)
    sal_year = Column(Integer)
    sal_month = Column(Integer)


class ViwGstInvoiceDetails(Base):
    __tablename__ = 'viw_gst_invoice_details'

    invoice_mst_com_pk = Column(String, primary_key=True)
    slno = Column(Integer)
    hsn_sac = Column(String)
    invoice_date = Column(Date)
    product_service_desc = Column(String)
    unit_of_measurement = Column(String)
    currency_type = Column(String)
    quantity = Column(Numeric)
    rate = Column(Numeric)
    amount = Column(Numeric)
    discount = Column(Numeric)
    base_amount = Column(Numeric)
    gst_rate = Column(Numeric)
    igst_amount = Column(Numeric)
    cgst_amount = Column(Numeric)
    sgst_amount = Column(Numeric)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)


class ViwGstInvoiceMst(Base):
    __tablename__ = 'viw_gst_invoice_mst'

    org_id = Column(String, primary_key=True)
    project_id = Column(String)
    invoice_date = Column(Date)
    invoice_no = Column(String)
    supplier_id = Column(String)
    hsn_sac = Column(String)
    reverse_charges = Column(String)
    invoice_amount = Column(Numeric)
    base_amount = Column(Numeric)
    customer_id = Column(String)
    consignee_id = Column(String)
    consignee_name = Column(String)
    supply_date = Column(DateTime)
    supply_state = Column(String)
    goods_or_service = Column(String)
    gst_rate = Column(Numeric)
    tot_igst_amount = Column(Numeric)
    tot_cgst_amount = Column(Numeric)
    tot_sgst_amount = Column(Numeric)
    cess = Column(Numeric)
    tds = Column(Numeric)
    invoice_status = Column(String)
    remarks = Column(String)
    invoice_mst_com_pk = Column(String)
    reference_id = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)


class ViwInstAccountsCrfBilDetails(Base):
    __tablename__ = 'viw_inst_accounts_crf_bil_details'

    booking_request_id = Column(String)
    booking_id = Column(String)
    bill_no = Column(String, primary_key=True)
    voucher_no = Column(String)
    voucher_date = Column(String)
    chq_dd_tv_no = Column(String)
    payee_id = Column(String)
    payment_status = Column(String)
    bill_desc = Column(String)
    verified_amt = Column(Numeric)


class ViwInstAssetMaster(Base):
    __tablename__ = 'viw_inst_asset_master'

    fin_year = Column(String, primary_key=True)
    org_name = Column(String)
    cost_centre_name = Column(String)
    project_name = Column(String)
    asset_id = Column(String)
    asset_group_description = Column(String)
    coa = Column(String)
    asset_description = Column(String)
    measuring_unit = Column(String)
    quantity = Column(Integer)
    inr_cost = Column(Numeric)
    foreign_cost = Column(Numeric)
    foreign_currency = Column(String)
    accumulated_cost = Column(Numeric)
    accumulated_depreciation = Column(Numeric)
    asset_depriciation_rate = Column(Numeric)
    asset_location = Column(String)
    sub_order_id = Column(String)
    initial_po_wo_oo_ref = Column(String)
    asset_state = Column(String)
    insurance_coverage = Column(Numeric)
    warranty = Column(String)
    placed_in_service = Column(Text)
    estimated_life_in_days = Column(Integer)
    depreciation_start_date = Column(Text)
    salvage_value = Column(Numeric)
    asset_entry_as = Column(String)
    billno = Column(String)
    asset_status = Column(String)
    tangiable = Column(String)


class ViwInstBillDetails(Base):
    __tablename__ = 'viw_inst_bill_details'

    fin_year = Column(String, primary_key=True)
    org_id = Column(String)
    bill_no = Column(Integer)
    slno = Column(Integer)
    payee_id = Column(String)
    voucher_no = Column(Integer)
    dr_amt = Column(Numeric)
    payee_info = Column(String)
    bill_state_mst_pk = Column(String)
    payment_flag = Column(String)
    chq_dd_tv_no = Column(String)
    payment_date = Column(DateTime)
    actual_payee_id = Column(String)


class ViwInstBillDiaryEntry(Base):
    __tablename__ = 'viw_inst_bill_diary_entry'

    org_id = Column(String, primary_key=True)
    req_date = Column(Date)
    slno = Column(Integer)
    payee_id = Column(String)
    reference_id = Column(String)
    description = Column(String)
    applied_amount = Column(Numeric)
    verified_amount = Column(Numeric)
    bill_state_mst_pk = Column(String)
    bill_diary_entry_com_pk = Column(String)
    request_status = Column(String)


class ViwInstIfscMst(Base):
    __tablename__ = 'viw_inst_ifsc_mst'

    ifsc = Column(String, primary_key=True)
    bank = Column(String)
    micr = Column(String)
    branch = Column(String)
    address = Column(String)
    contact = Column(String)
    city = Column(String)
    district = Column(String)
    state = Column(String)


class ViwInstVendorMst(Base):
    __tablename__ = 'viw_inst_vendor_mst'

    vendor_code = Column(String, primary_key=True)
    vendor_name = Column(String)
    pan_no = Column(String)
    bank_ac_no = Column(String)
    ifsc_code = Column(String)
    micr_code = Column(String)
    swift_code = Column(String)
    holding_premise = Column(String)
    street_name = Column(String)
    room_no = Column(String)
    floor = Column(String)
    city_village_town = Column(String)
    district = Column(String)
    state = Column(String)
    country = Column(String)
    pin = Column(String)
    email = Column(String)
    contact_number = Column(String)
    reg_date = Column(String)
    status_flag = Column(String)
    status_update_date = Column(DateTime)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    old_vendor_code = Column(String)
    gstin = Column(String)
    sric_vendor_code = Column(String)
    composite_scheme = Column(String)


class ViwItaxauthority(Base):
    __tablename__ = 'viw_itaxauthority'

    finyear = Column(String, primary_key=True)
    empno = Column(String)
    digisign_state = Column(String)


class ViwItaxRate(Base):
    __tablename__ = 'viw_itax_rate'

    finyear = Column(String, primary_key=True)
    sex = Column(String)
    from_amt = Column(String)
    to_amt = Column(String)
    rate = Column(String)
    min_amt = Column(String)
    surcharge = Column(String)
    cess = Column(String)


class ViwItrComplianceSection206(Base):
    __tablename__ = 'viw_itr_compliance_section_206'

    fin_year = Column(String, primary_key=True)
    pan_no = Column(String)
    name = Column(String)
    pan_aadhar_link_status = Column(String)
    nc_us_206 = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    pan_allot_date = Column(String)


class ViwMiscmas(Base):
    __tablename__ = 'viw_miscmas'

    code = Column(String, primary_key=True)
    name = Column(String)
    gender = Column(String)
    highestedu = Column(String)
    dob = Column(Date)
    doj = Column(Date)
    dor = Column(Date)
    desg = Column(String)
    dept = Column(String)
    place_of_posting = Column(String)
    in_service = Column(String)
    attachment_type = Column(String)
    old_empno = Column(String)
    oo_number = Column(String)
    present_add = Column(String)
    present_street = Column(String)
    present_city = Column(String)
    present_state = Column(String)
    present_country = Column(String)
    present_pin = Column(String)
    org_add = Column(String)
    org_street = Column(String)
    org_city = Column(String)
    org_state = Column(String)
    org_country = Column(String)
    org_pin = Column(String)
    mobile_no = Column(String)
    org_phone = Column(String)
    org_fax = Column(String)
    present_phone = Column(String)
    present_fax = Column(String)
    bank_name = Column(String)
    bank_address = Column(String)
    ifsc_code = Column(String)
    micr_code = Column(String)
    account_no = Column(String)
    pan_no = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    modify_by = Column(String)
    modification_date = Column(DateTime)
    delete_flag = Column(String)
    before_name = Column(String)
    org_desg = Column(String)
    last_experience = Column(String)
    from_institute = Column(String)
    payment_rate = Column(Numeric)
    payment_basis = Column(String)
    email = Column(String)


class ViwPanDetails(Base):
    __tablename__ = 'viw_pan_details'

    account_no = Column(String)
    user_code = Column(String, primary_key=True)
    pan_no = Column(String)
    pan_cha = Column(Text)
    emp_type = Column(Text)
    bank_name = Column(String)
    micr = Column(String)
    ifsc = Column(String)
    bank_address = Column(String)


class ViwPfmsComponentCodeCoaMapping(Base):
    __tablename__ = 'viw_pfms_component_code_coa_mapping'

    org_id = Column(String, primary_key=True)
    scheme_id = Column(String)
    coa = Column(Integer)
    component_code = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)


class ViwPfmsComponents(Base):
    __tablename__ = 'viw_pfms_components'

    org_id = Column(String, primary_key=True)
    scheme_id = Column(String)
    component_code = Column(String)
    component_name = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)
    active_flag = Column(String)


class ViwPfmsSchemes(Base):
    __tablename__ = 'viw_pfms_schemes'

    scheme_id = Column(String, primary_key=True)
    org_id = Column(String)
    scheme_description = Column(String)
    activated_from = Column(DateTime)
    activated_to = Column(DateTime)
    active_status = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)
    modified_by = Column(String)
    modification_time = Column(DateTime)


class ViwPgStudentmas(Base):
    __tablename__ = 'viw_pg_studentmas'

    rollno = Column(String, primary_key=True)
    name = Column(String)
    dept = Column(String)
    hall = Column(String)
    mail_state = Column(String)
    bank_acc_no = Column(String)


class ViwProjectBudgetAllocatedHead(Base):
    __tablename__ = 'viw_project_budget_allocated_head'

    parent_acc_desc = Column(String)
    account_description = Column(String)
    parent_acc_code = Column(Integer)
    account_code = Column(Integer)
    unbounded_fund_flag = Column(String)
    proj_unbounded_fund_flag = Column(String)
    project_code = Column(Integer, primary_key=True)


class ViwResearchQualification(Base):
    __tablename__ = 'viw_research_qualification'

    rollno = Column(String, primary_key=True)
    slno = Column(String)
    qualification = Column(String)
    university = Column(String)
    degree = Column(String)
    year = Column(String)
    percentage = Column(String)
    subjects = Column(String)


class ViwRsRegistrationSeminar(Base):
    __tablename__ = 'viw_rs_registration_seminar'

    rollno = Column(String, primary_key=True)
    sl_no = Column(Integer)
    final_seminar = Column(String)
    date_of_seminar = Column(DateTime)
    attendance = Column(String)
    problem_definition = Column(String)
    problem_definition_comment = Column(String)
    literature_survey = Column(String)
    literature_survey_comment = Column(String)
    report = Column(String)
    report_comment = Column(String)
    seminar_presentation = Column(String)
    seminar_presentation_comment = Column(String)
    remarks = Column(String)
    comprehensive_exam_result = Column(String)
    registered_date = Column(DateTime)
    recommended_date = Column(DateTime)
    recommendation = Column(String)
    dean_approval = Column(String)
    user_code = Column(String)


class ViwRsStudentmas(Base):
    __tablename__ = 'viw_rs_studentmas'

    rollno = Column(String, primary_key=True)
    name = Column(String)
    dept = Column(String)
    email = Column(String)


class ViwSalscaleMaster(Base):
    __tablename__ = 'viw_salscale_master'

    slno = Column(Integer, primary_key=True)
    scale_ind = Column(String)
    min_basic = Column(String)
    max_basic = Column(String)
    incr_rate = Column(String)
    eb_reqd = Column(String)
    abcd = Column(String)
    scale_desc = Column(String)


class ViwServiceContractList(Base):
    __tablename__ = 'viw_service_contract_list'

    project_code = Column(Integer, primary_key=True)
    application_no = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    office_order_no = Column(String)
    account_code = Column(Integer)


class ViwSric89daysStaffList(Base):
    __tablename__ = 'viw_sric_89days_staff_list'

    serial_no = Column(String, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    phone = Column(String)
    dob = Column(String)
    guardian_name = Column(String)
    nationality = Column(String)
    bank_name = Column(String)
    bank_address = Column(String)
    bank_ifsc = Column(String)
    bank_acc_no = Column(String)
    ref_no = Column(String)
    pan = Column(String)
    user_project_code = Column(String)
    project_code = Column(String)
    from_date = Column(Date)
    to_date = Column(Date)
    amount = Column(Float)
    guide_id = Column(String)
    dept = Column(String)
    job_desc = Column(String)
    installment_no = Column(Integer)
    office_order_no = Column(String)
    city = Column(String)
    state = Column(String)
    address = Column(String)


class ViwSricAssetRegister(Base):
    __tablename__ = 'viw_sric_asset_register'

    financial_year = Column(String)
    project_code = Column(Integer, primary_key=True)
    user_project_code = Column(String)
    project_start_date = Column(Date)
    project_end_date = Column(Date)
    pi_copi = Column(String)
    custodian = Column(String)
    purchase_order_no = Column(String)
    purchase_oder_date = Column(Date)
    code_of_supplier = Column(String)
    remarks = Column(String)
    inst_ref_no = Column(String)
    cost_amount = Column(Float)
    invoice_no = Column(String)
    invoice_date = Column(Text)
    payment_voucher_no = Column(String)
    payment_amt = Column(Text)
    payment_voucher_date = Column(Text)
    bill_owner_name = Column(String)
    sric_purchase_order = Column(String)


class ViwSricSalaryVsrcRoomRentAllocation(Base):
    __tablename__ = 'viw_sric_salary_vsrc_room_rent_allocation'

    vsrc_id = Column(String, primary_key=True)
    yr = Column(String)
    mon = Column(String)
    room_type = Column(String)
    room_id = Column(String)
    room_rent = Column(Numeric)
    demand_no = Column(String)
    allotment_from_date = Column(Date)
    allotment_to_date = Column(Date)


class ViwSsoUserMaster(Base):
    __tablename__ = 'viw_sso_user_master'

    user_code = Column(Text, primary_key=True)
    user_detail_code = Column(Text)
    user_type = Column(Text)
    alias = Column(Text)
    alias_password = Column(Text)
    signedflag = Column(Text)


class ViwStakeholderQualificationApp(Base):
    __tablename__ = 'viw_stakeholder_qualification_app'

    stakeholder_code = Column(String)
    sl_no = Column(Numeric, primary_key=True)
    edu_type = Column(String)
    degree = Column(String)
    uni_inst = Column(String)
    pass_year = Column(String)
    dicipline = Column(String)
    div_cls = Column(String)
    marks_per = Column(String)
    rank = Column(String)
    institute = Column(String)
    total_marks = Column(String)
    persentage_marks = Column(String)
    del_flag = Column(String)
    supporting_file = Column(String)
    approve_flag = Column(String)
    approve_by = Column(String)
    approval_time = Column(DateTime)
    highest_acad_flag = Column(String)


class ViwStateMst(Base):
    __tablename__ = 'viw_state_mst'

    state_code = Column(Integer, primary_key=True)
    state_name = Column(String)
    state_initial = Column(String)
    state_type = Column(String)


class ViwStudentmasRs(Base):
    __tablename__ = 'viw_studentmas_rs'

    rollno = Column(String, primary_key=True)
    name = Column(String)
    department = Column(String)
    category = Column(String)
    status = Column(String)
    gatenet = Column(String)
    year = Column(String)
    assistantrateforfirstyear = Column(String)
    residentialtype = Column(String)
    dateofjoining = Column(Date)
    dateofdscformation = Column(String)
    dateofenrolment = Column(String)
    datofregistrationseminar = Column(String)
    dateofsynopsisseminar = Column(String)
    dateofsubmissionofthesis = Column(String)
    dateofvivavoce = Column(String)
    dateofawarddegree = Column(String)
    bloodgroup = Column(String)
    enhancemetseminardate = Column(String)
    extension1seminardate = Column(String)
    extension2seminardate = Column(String)
    specialisation = Column(String)
    extensionin3rdyear = Column(String)
    email = Column(String)
    phone = Column(String)
    flag = Column(String)
    session = Column(String)
    semester = Column(String)
    filecode = Column(String)
    cellno = Column(String)
    address1 = Column(String)
    address2 = Column(String)
    nationality = Column(String)
    dateofbirth = Column(Date)
    gender = Column(String)
    otherrem = Column(String)
    locktable = Column(String)
    password = Column(String)
    enrolment = Column(String)
    edate = Column(Date)
    renewal = Column(String)
    rdate = Column(String)
    enhancement = Column(String)
    endate = Column(String)
    firstextension = Column(String)
    fedate = Column(String)
    secondextension = Column(String)
    sedate = Column(String)
    registration = Column(String)
    regdate = Column(String)
    tsubmission = Column(String)
    tsdate = Column(String)
    phdtermination = Column(String)
    ptdate = Column(String)
    filecode1 = Column(String)
    programleft = Column(String)
    phdreportarrived = Column(String)
    categorychange = Column(String)
    depttchanged = Column(String)
    ssubmission = Column(String)
    ssdate = Column(Date)
    projectcode = Column(String)
    piname = Column(String)
    dateprojectends = Column(String)
    convocation = Column(Integer)
    onrole = Column(String)
    dscs = Column(String)
    grades = Column(String)
    registrations = Column(String)
    renewals = Column(String)
    enhancements = Column(String)
    extensions = Column(String)
    fifthyexts = Column(String)
    cexams = Column(String)
    synopsiss = Column(String)
    panelofexs = Column(String)
    tabulationsheets = Column(String)
    extensions1 = Column(String)
    synopsisms = Column(String)
    photo_image_path = Column(String)
    sign_image_path = Column(String)
    photo_image_name = Column(String)
    sign_image_name = Column(String)
    joining_conf_flag = Column(String)
    adhaar_card_no = Column(Numeric)


class ViwUgStudentmas(Base):
    __tablename__ = 'viw_ug_studentmas'

    rollno = Column(String, primary_key=True)
    deptcode = Column(String)
    coursecode = Column(String)
    name = Column(String)
    longname = Column(String)
    hall = Column(String)
    room = Column(String)
    father_name = Column(String)
    guardian_name = Column(String)
    nationality = Column(String)
    country = Column(String)
    native_state = Column(String)
    mother_tongue = Column(String)
    date_of_birth = Column(DateTime)
    sex = Column(String)
    category = Column(String)
    blood_group = Column(String)
    height_in_cms = Column(Numeric)
    weight_in_kgs = Column(Numeric)
    mail_addr1 = Column(String)
    mail_addr2 = Column(String)
    mail_addr3 = Column(String)
    mail_addr4 = Column(String)
    perm_addr1 = Column(String)
    perm_addr2 = Column(String)
    perm_addr3 = Column(String)
    perm_addr4 = Column(String)
    telephone_no = Column(String)
    fat_guar_mincome = Column(Numeric)
    guar_annual_inc = Column(String)
    parental_profess = Column(String)
    foreign_passport = Column(String)
    nature_of_admission = Column(String)
    jee_regno = Column(String)
    all_india_rank = Column(Integer)
    year_of_admiss = Column(String)
    qual_exam_year = Column(String)
    qual_exam_name = Column(String)
    board_univ_name = Column(String)
    percent_marks = Column(Numeric)
    hs_educa_area = Column(String)
    hs_educ_medium = Column(String)
    from_semester = Column(Integer)
    dep_change_roll = Column(String)
    repeat_case_roll = Column(String)
    course_complete = Column(Integer)
    bank_acc_no = Column(String)
    opid = Column(String)
    section = Column(String)
    year_of_pass = Column(Integer)
    degree_type = Column(String)
    punish_flag = Column(String)
    year_rate = Column(String)
    reside_status = Column(String)
    rollno_old = Column(String)
    minor_status = Column(String)
    minor_coursename = Column(String)
    branch_ch_flag = Column(String)
    e_mail = Column(String)
    section1 = Column(String)
    curr_year = Column(Integer)
    cat_air = Column(String)


class ViwUserDetails(Base):
    __tablename__ = 'viw_user_details'

    user_code = Column(String, primary_key=True)
    alias = Column(String)
    alias_password = Column(String)
    empno = Column(String)
    empname = Column(String)
    desg_code = Column(String)
    desg = Column(String)
    dept_code = Column(String)
    depname = Column(String)


class ViwUserRoleDetail(Base):
    __tablename__ = 'viw_user_role_detail'

    user_code = Column(String, primary_key=True)
    role_code = Column(Integer)
    activated_from = Column(Date)
    activated_to = Column(Date)
    access_status = Column(String)


class ViwVendorApplicableFor194q(Base):
    __tablename__ = 'viw_vendor_applicable_for_194q'

    fin_year = Column(String, primary_key=True)
    bill_date = Column(Date)
    voucher_date = Column(Date)
    org_id = Column(String)
    payee_id = Column(String)
    vendor_name = Column(String)
    pan_no = Column(String)
    gstin = Column(String)
    cr_head_id = Column(String)
    head_name = Column(String)
    total_pay_amount = Column(Numeric)
    bill_no = Column(String)
    description = Column(String)


class ViwVendorMaster(Base):
    __tablename__ = 'viw_vendor_master'

    vendor_code = Column(String, primary_key=True)
    vendor_name = Column(String)
    vendor_address = Column(String)
    pan_no = Column(String)
    bank_ac_no = Column(String)
    bank_code = Column(String)
    bank_address = Column(String)
    phone_no = Column(String)
    branch_name = Column(String)
    micr = Column(String)
    delete_flag = Column(String)
    vendor_type = Column(String)
    vat_no = Column(String)
    mail_id = Column(String)
    contact_person = Column(String)
    telephone = Column(String)
    fax = Column(String)
    benificiary_name = Column(String)
    benificiary_add = Column(String)
    lock_flag = Column(String)
    ins_id = Column(String)
    service_tax_no = Column(String)


class ViwVendorMaster2(Base):
    __tablename__ = 'viw_vendor_master_2'

    vendor_code = Column(String, primary_key=True)
    vendor_name = Column(String)
    vendor_address = Column(String)
    pan_no = Column(String)
    bank_ac_no = Column(String)
    bank_code = Column(String)
    bank_address = Column(String)
    phone_no = Column(String)
    branch_name = Column(String)
    delete_flag = Column(String)


class VsrcAllocation(Base):
    __tablename__ = 'vsrc_allocation'

    sl_no = Column(Integer, primary_key=True)
    block = Column(String, nullable=False)
    room = Column(String, nullable=False)
    bed = Column(String, nullable=False)
    sric_id = Column(String, nullable=False)
    applicant = Column(String, nullable=False)
    from_date = Column(Date)
    from_time = Column(String)
    to_date = Column(Date)
    to_time = Column(String)
    remarks = Column(String)
    email_id = Column(String)
    phone_no = Column(String)
    asset_remarks = Column(String)
    applicant_type = Column(String)
    project_code = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)
    mess_block = Column(String)
    meass_room = Column(String)
    mess_allocation_date = Column(Date)
    mess_remarks = Column(String)
    guest_ref_name = Column(String)
    guest_ref_code = Column(String)
    sao_ar_signed_file_name = Column(String)
    sao_ar_signed_file_path = Column(String)
    sao_ar_signed_by = Column(String)
    sao_ar_signed_date = Column(DateTime)
    send_mail = Column(String, nullable=False)
    mail_date = Column(DateTime)


class VsrcBlockRoomBed(Base):
    __tablename__ = 'vsrc_block_room_bed'

    block = Column(String, primary_key=True)
    room = Column(String, nullable=False)
    bed = Column(String, nullable=False)
    allocation = Column(String)
    room_type = Column(String)
    accomodation_type = Column(String)
    rate = Column(Numeric)


class VsrcMaster(Base):
    __tablename__ = 'vsrc_master'

    block = Column(String, primary_key=True)
    room = Column(String, nullable=False)
    bed = Column(String, nullable=False)
    rate = Column(Numeric)
    activated_from = Column(Date)
    from_time = Column(String)
    activated_to = Column(Date)
    to_time = Column(String)
    allocation_status = Column(String)
    room_type = Column(String)
    remarks = Column(String)
    created_by = Column(String)
    creation_date = Column(DateTime)
    delete_flag = Column(String, nullable=False)


class WorkDelegation(Base):
    __tablename__ = 'work_delegation'

    menu_id = Column(Integer, primary_key=True)
    delegated_by = Column(String, nullable=False)
    delegated_to = Column(String, nullable=False)
    attr_name = Column(String)
    attr_value = Column(String, nullable=False)
    from_date = Column(Date)
    to_date = Column(Date)
    stop_access = Column(String)
    created_by = Column(String)
    creation_time = Column(DateTime)


class WorkflowTransactionHistory(Base):
    __tablename__ = 'workflow_transaction_history'

    process_id = Column(String, nullable=False)
    version_id = Column(Integer, nullable=False)
    instance_id = Column(String, nullable=False)
    instance_year = Column(String, nullable=False)
    serial_no = Column(Integer, primary_key=True)
    from_node = Column(String)
    to_node = Column(String)
    status = Column(String)
    remarks = Column(String)
    sent_by = Column(String)
    sent_at = Column(DateTime)
    seq = Column(Integer)

