import { TestBed } from '@angular/core/testing';

import { JobsiteDataService } from './jobsite-data.service';

describe('JobsiteDataService', () => {
  let service: JobsiteDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(JobsiteDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
