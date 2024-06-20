icacls.exe carzone-key.pem /reset
icacls.exe carzone-key.pem /grant:r "$($env:username):(r)"
icacls.exe carzone-key.pem /inheritance:r
