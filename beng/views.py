from django.shortcuts import redirect,render
from .models import donor, blooddetails, bloodbank, hospital, employee, bloodrequest
from .forms import bloodForm
def mainpage(request):

	return render(request,'home.html')
	

def firstpage(request):
	russel=donor.objects.all()
	villareal=blooddetails.objects.all()
	context ={'russel':russel,'villareal':villareal}
	return render(request,'donor.html', context)

def secondpage(request):
	donorId=donor.objects.create(
		donor_name = request.POST['donor_name'],
		phone_number = request.POST['phone_number'],
		age = request.POST['age'],
		date_of_birth = request.POST['date_of_birth'],
		address = request.POST['address'],
		gender = request.POST['gender'],
		)
	BloodId=blooddetails.objects.create(
		bb_blood = request.POST['blood_type'],
		blood_bag_number = request.POST['blood_bag_number'],
		date_extracted = request.POST['date_extracted'],
		remarks = request.POST['message'],
		)
	return redirect('Donor')
	return render(request,'donor.html')
	
def Patient(request):
	BloodId=bloodbank.objects.create(
		name = request.POST['happy'],
		telephone_number = request.POST['telephone_number'],
		blood_bank_address = request.POST['blood_bank_address'],
		quantity_received = request.POST['quantity_received'],
		description = request.POST['descriptione'],
		)
	hospitaal=hospital.objects.create(
		hospital_name = request.POST['hospital_name'],
		phone_number = request.POST['phone_number'],
		hospital_address = request.POST['hospital_address'],
		)
	hospitalId=employee.objects.create(
		employee_name = request.POST['employee_name'],
		employee_phone_number = request.POST['employee_phone_number'],
		employee_Address = request.POST['employee_Address'],
		employee_position = request.POST['employee_position'],
		)
	return redirect('request')
	return render(request,'bank.html')

def Donor(request):
	
	return render(request,'bank.html')


def request(request):

	return render(request,'request.html')

def Last(request):
	superlast=bloodrequest.objects.create(
		date = request.POST['date'],
		quantity = request.POST['quantity'],
		bld_typ_req = request.POST['bld_type_req'],
		recipient_name = request.POST['recipient_name'],
		)

	return render(request,'request.html')


def about(request):

	return render(request,'about.html')



def updateblood(request, pk):

	russel = blooddetails.objects.get(id=pk)
	form = bloodForm(instance=russel)

	if request.method == 'POST':
		form = bloodForm(request.POST, instance=russel)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'update.html', context)

def deleteblood(request, pk):
	russel = blooddetails.objects.get(id=pk)
	if request.method == "POST":
		russel.delete()
		return redirect('/')

	context = {'item':russel}
	return render(request, 'delete.html', context)
