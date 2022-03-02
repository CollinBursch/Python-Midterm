from pickle import TRUE
import PatientClass as PatC
import ProcedureClass as ProC

def main():
    # Making an instance of the PatientClass and holding it in patient variable 
    patient = PatC.PatientClass(1, 'Matt Jones', '123 Main st, Waco TX 76706', '254-555-7415', True) 
    procedure_list = []
    procedure_list.append(ProC.ProcedureClass('Physical Exam', '2/15/2022', 'Dr. Irvine', 250, 1))
    procedure_list.append(ProC.ProcedureClass('MRI', '2/15/2022', 'Dr. Hamilton', 1500, 1))
    procedure_list.append(ProC.ProcedureClass('CT Scan', '2/17/2022', 'Dr. Drey', 1200, 2))

    print('*** Patient Bill ***')
    print('Name:', patient.get_name())
    print('Address:', patient.get_address())
    print('Phone:', patient.get_phone())
    print()

    total_charge = 0
    for procedure in procedure_list:
        if patient.get_ID() == procedure.get_patient_ID() :
            print('Procedure:', procedure.get_name())
            print('Date:', procedure.get_date())
            print('Pactitioner:', procedure.get_practitioner())
            print('Charge: ${:,.2f}'.format(procedure.get_charges()), sep='')
            print()
            if patient.get_veteran_status() == True:
                total_charge += procedure.get_charges() * .60
            else:
                total_charge += procedure.get_charges()
                

    print('Total Charges: ${:,.2f}'.format(total_charge), sep='')

main()
