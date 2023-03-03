import { Component, OnInit } from '@angular/core';
import { JobsiteDataService } from 'src/app/services/jobsite-data.service';

@Component({
  selector: 'app-home-main-job',
  templateUrl: './home-main-job.component.html',
  styleUrls: ['./home-main-job.component.css']
})
export class HomeMainJobComponent implements OnInit {

  public Job_Lists = [] as any;

  constructor ( private _job_Function_Services : JobsiteDataService ){}

  ngOnInit(): void {
    this._job_Function_Services.getJobsite_JobList().subscribe((data) => {
      this.Job_Lists = data
    })
  }

}
