import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class JobsiteDataService {

  private urlApi = 'http://127.0.0.1:8090'

  constructor( private http : HttpClient) { }

  getJobsite_jobFunction(){
    return this.http.get(this.urlApi + `/joblist-api/job-function/`);
  }

  getJobsite_JobList(){
    return this.http.get(this.urlApi + `/joblist-api/job-list/`);
  }

}

