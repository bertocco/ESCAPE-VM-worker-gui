# New view for dynamic content:
from django.shortcuts import render
from django.http import HttpResponseRedirect

#from . models import CreateVM
from . forms import CreatevmForm

from . api.esap_fedcloud_client import create_public_vm

# Set fixed (for proof of concept) parameters
site = "CESGA"
vo = "vo.access.egi.eu"
# Fix other values for demo
flavour_selected = "cor2mem4hd20"
image_selected = "Image for EGI Ubuntu 20.04 [Ubuntu/20.04/VirtualBox]"
network_selected = "net-vo.access.egi.eu"
public_network = "public00"

def createvm(request):
    submitted=False
    IP = ""
    if request.method == 'POST':
        form = CreatevmForm(request.POST)
        access_token_value = request.POST["access_token"]
        machine_name_value = request.POST["machine_name"]
        ssh_access_key_name_value = request.POST["ssh_access_key"]
        print("ACCESS TOKEN received in view:")
        print("###" + access_token_value + "###")
        err_code, IP = create_public_vm(access_token_value, site, vo, flavour_selected, image_selected, network_selected, ssh_access_key_name_value, machine_name_value, public_network)
        if(err_code != 0):
            #return HttpResponseRedirect('createvm_error.html?error=' + IP)
            return render(request, 'createvm/createvm_error.html', {'error': IP})
        else:
            #return HttpResponseRedirect('createvm_success.html', {'createvmform': form})
            return render(request, 'createvm/createvm_success.html', {'vmname': machine_name_value, 'pubip': IP})
    else:
        form = CreatevmForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'createvm/createvm.html', {'createvmform': form, 'submitted': submitted})

