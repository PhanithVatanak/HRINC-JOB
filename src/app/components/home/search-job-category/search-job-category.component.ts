import { Component, OnInit } from '@angular/core';
import { JobsiteDataService } from 'src/app/services/jobsite-data.service';
import {FormControl} from '@angular/forms';
import {Observable} from 'rxjs';
import {map, startWith} from 'rxjs/operators';


interface Food {
  value: string;
  viewValue: string;
}

@Component({
  selector: 'app-search-job-category',
  templateUrl: './search-job-category.component.html',
  styleUrls: ['./search-job-category.component.css']
})
export class SearchJobCategoryComponent implements OnInit {

  public Job_Functions = [] as any;

  constructor ( private _job_Function_Services : JobsiteDataService ) {}

  ngOnInit(): void {
      this._job_Function_Services.getJobsite_jobFunction().subscribe((data) => {
        this.Job_Functions = data
      })
  }
}
