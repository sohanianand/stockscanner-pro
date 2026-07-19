import api from "./api";

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export const login = async (
  request: LoginRequest
): Promise<LoginResponse> => {
  const response = await api.post<LoginResponse>(
    "/auth/login",
    request
  );

  return response.data;
};

export const register = async (request: any) => {
  const response = await api.post(
    "/auth/register",
    request
  );

  return response.data;
};
