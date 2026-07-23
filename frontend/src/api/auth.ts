import api from "./client";

export interface LoginRequest {
  username: string;
  password: string;
}

export interface User {
  id?: string | number;
  username?: string;
  name?: string;
}

export interface LoginResponse {
  token?: string;
  access_token?: string;
  user?: User;
  message?: string;
}

export async function login(
  data: LoginRequest
): Promise<LoginResponse> {
  const response = await api.post<LoginResponse>(
    "/auth/login",
    data
  );

  return response.data;
}
