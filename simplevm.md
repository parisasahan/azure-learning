# 🖥️ Create a Simple Virtual Machine on Azure (GUI)

## 🎯 Objective
Create a virtual machine using the Azure Portal with step-by-step instructions and GUI screenshots.

---

## 📋 Prerequisites
- An active [Azure account](https://portal.azure.com)
- Basic knowledge of cloud and VMs
- Internet connection

---

## 🚀 Steps to Create the VM

### 🔐 1. Sign in to Azure Portal
- Go to: [https://portal.azure.com](https://portal.azure.com)
- Enter your login credentials.

![Azure Login Page](images/azure-login.png)

---

### 📦 2. Search for "Virtual Machines"
- On the homepage, use the top search bar and type `Virtual Machines`.
- Click on the result.

![Search Virtual Machines](images/search-vm.png)

---

### ➕ 3. Click “Create” > “Virtual Machine”
- On the Virtual Machines page, click the `+ Create` button.
- Then choose `Azure virtual machine`.

![Create VM Button](images/create-vm.png)

---

### 📝 4. Configure the Basic Settings
- **Subscription**: Select your active subscription.
- **Resource group**: Create new (e.g., `MyVMGroup`) or use an existing one.
- **Virtual machine name**: `MyFirstVM`
- **Region**: Choose closest to your location (e.g., `East US`)
- **Image**: `Windows Server 2019` or `Ubuntu 20.04`
- **Size**: Choose `Standard_B1s` (cheap & basic)
- **Authentication type**: Password or SSH
- **Username**: `azureuser`
- **Password**: Create a strong one

![Basic Settings](images/basic-settings.png)

---

### 🌐 5. Configure Networking (Optional)
- Keep default settings or create a new virtual network.
- Ensure Public IP is enabled.
- Allow selected ports (e.g., SSH for Linux or RDP for Windows).

![Networking Settings](images/networking-settings.png)

---

### ✅ 6. Review + Create
- Click `Next` until you reach the **Review + Create** tab.
- Review all your settings.
- Click the `Create` button.

![Review and Create](images/review-create.png)

---

### ⏳ 7. Deployment in Progress
- Azure will begin deploying your VM.
- You’ll see a progress bar and confirmation when done.

![Deployment Progress](images/deployment.png)

---

### 🟢 8. Connect to Your VM
- Go back to the Virtual Machines dashboard.
- Select your VM (`MyFirstVM`).
- Click **Connect** > choose `RDP` (Windows) or `SSH` (Linux).
- Follow the instructions to access your VM.

![Connect to VM](images/connect-vm.png)

---

## 🧽 Clean Up (Optional)
To avoid charges, delete the VM and its resources:
- Go to the Resource Group > Click `Delete Resource Group`.

---

## 📚 References
- [Azure VM Documentation](https://learn.microsoft.com/en-us/azure/virtual-machines/)
- [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/)

