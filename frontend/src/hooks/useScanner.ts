import { useMutation } from "@tanstack/react-query";

import { runScanner } from "../api/scanner";

export function useScanner() {

  return useMutation({

    mutationFn: runScanner,

  });

}
