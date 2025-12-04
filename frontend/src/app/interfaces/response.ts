export interface IResponse<T> {
  status_code: number;
  body: T;
  message?: string;
}
