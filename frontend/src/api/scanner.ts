import api from "./api";
import {
  ScannerRequest,
  ScannerResponse,
} from "../types/scanner";

export async function runScanner(
  request: ScannerRequest
): Promise<ScannerResponse> {

  const response = await api.post(
    "/scanner/scan",
    request
  );

  return response.data;
}

export async function saveScanner(
  request: any
) {

  const response = await api.post(
    "/saved-scanners",
    request
  );

  return response.data;
}

export async function getSavedScanners() {

  const response = await api.get(
    "/saved-scanners"
  );

  return response.data;
}
