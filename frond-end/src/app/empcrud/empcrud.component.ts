import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-empcrud',
  templateUrl: './empcrud.component.html',
  styleUrls: ['./empcrud.component.scss']
})
export class CrudComponent implements OnInit {
  branch: any[] = [];
  employee: any[] = [];
  branchFormValues: any = {};
  employeeFormValues: any = {};
  branchFormTitle: string = 'Create Branch';
  employeeFormTitle: string = 'Create Employee';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.getBranch();
    this.getEmployee();
  }

  getBranch() {
    this.http.get<any>('http://localhost:8000/branch/').subscribe(data => {
      this.branch = data;
    });
  }

  getEmployee() {
    this.http.get<any>('http://localhost:8000/employee/').subscribe(data => {
      this.employee = data;
    });
  }

  submitBranchForm() {
    if (this.branchFormValues.branch_id) {
      this.updateBranch();
    } else {
      this.createBranch();
    }
  }

  createBranch() {
    this.http.post<any>('http://localhost:8000/branch/', this.branchFormValues).subscribe(data => {
      this.getBranch();
      this.resetBranchForm();
    });
  }

  updateBranch() {
    this.http.put<any>(`http://localhost:8000/branch/${this.branchFormValues.branch_id}/`, this.branchFormValues).subscribe(data => {
      this.getBranch();
      this.resetBranchForm();
    });
  }

  editBranch(branch: any) {
    this.branchFormValues = { ...branch };
    this.branchFormTitle = 'Edit Branch';
  }

  deleteBranch(branch: any) {
    this.http.delete<any>(`http://localhost:8000/branch/${branch.branch_id}/`).subscribe(data => {
      this.getBranch();
    });
  }

  submitEmployeeForm() {
    if (this.employeeFormValues.employee_id) {
      this.updateEmployee();
    } else {
      this.createEmployee();
    }
  }

  createEmployee() {
    this.http.post<any>('http://localhost:8000/employee/', this.employeeFormValues).subscribe(data => {
      this.getEmployee();
      this.resetEmployeeForm();
    });
  }

  updateEmployee() {
    this.http.put<any>(`http://localhost:8000/employee/${this.employeeFormValues.employee_id}/`, this.employeeFormValues).subscribe(data => {
      this.getEmployee();
      this.resetEmployeeForm();
    });
  }

  editEmployee(employee: any) {
    this.employeeFormValues = { ...employee };
    this.employeeFormTitle = 'Edit Employee';
  }

  deleteEmployee(employee: any) {
    this.http.delete<any>(`http://localhost:8000/employee/${employee.employee_id}/`).subscribe(data => {
      this.getEmployee();
    });
  }

  resetBranchForm() {
    this.branchFormValues = {};
    this.branchFormTitle = 'Create a Branch';
  }

  resetEmployeeForm() {
    this.employeeFormValues = {};
    this.employeeFormTitle = 'Create an Employee';
  }

  getBranchName(branchId: number) {
    const branch = this.branch.find(branch => branch.branch_id === branchId);
    return branch ? branch.name : 'No Branch';
  }

  getEmployeeName(employeeId: number) {
    const employee = this.employee.find(employee => employee.employee_id === employeeId);
    return employee ? employee.name : 'No Manager';
  }
}
