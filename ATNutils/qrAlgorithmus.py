import numpy as np
import scipy as cp

def main():
    A = np.array([
        [41, -12],
        [-12, 34]
    ])
    S = np.array([
        [0, 1],
        [1, 0]
    ])

    qrAlgorithmus(A, chatty=True, tol=0.003)
    qrAlgorithmus(A, chatty=True, shift="RayLeigh", tol=0.003)
    qrAlgorithmus(A, chatty=True, shift="Willkinson", tol=0.003)

def qrAlgorithmus(A, itterations=100, tol=10**-16, shift=None, chatty=False):
    """Finds Eigenvalues and Eigenvectors of A"""
    Ak = A.copy()
    Ek = np.eye(A.shape[0])

    for i in range(itterations + 1):
        ANext, ENext = _qrStep(Ak, Ek, shift)

        if (chatty):
            _printStep(Ak, Ek, i)

        if (np.allclose(Ak, ANext, atol=tol)):
            break;
        
        Ak = ANext
        Ek = ENext

    if(chatty):
        _printResult(A, Ak, Ek)

    return Ak, Ek

def _qrStep(Ak, Ek, shift):
    if (shift == "RayLeigh"):
        return _qrStepWithRayLeighShift(Ak, Ek)
    if(shift == "Willkinson"):
        return _qrStepWithWillkinsonShift(Ak, Ek)
    return _qrStepWithoutShift(Ak, Ek)

def _qrStepWithRayLeighShift(Ak, Ek):
    shape = Ak.shape[0]
    qk = Ak[-1, -1] * np.eye(shape)
    [Q, R] = np.linalg.qr(Ak - qk)
    AkNew = R @ Q + qk
    EkNew = Ek @ Q
    return AkNew, EkNew

def _qrStepWithWillkinsonShift(Ak, Ek):
    qk = _getQKWillkinson(Ak)
    [Q, R] = np.linalg.qr(Ak - qk)
    AkNew = R @ Q + qk
    EkNew = Ek @ Q
    return AkNew, EkNew

def _getQKWillkinson(Ak):
    ck = Ak[-1, -1]
    ak = Ak[-2, -2]
    bk = Ak[-1, -2]
    sk = 1 if ck > 0 else -1
    pk = 0.5 * (ak - ck)
    qk = ck - sk* (bk**2 / (np.abs(pk) + np.sqrt(pk**2 + bk**2)))
    return qk * np.eye(Ak.shape[0])

def _qrStepWithoutShift(Ak, Ek):
    [Q, R] = np.linalg.qr(Ak)
    AkNew = R @ Q
    EkNew = Ek @ Q
    return AkNew, EkNew

def _printStep(Ak, Ek, i):
    print(f"------ Itteration {i} ------")
    print(f"--- A{i} ---\n{Ak}")
    print(f"--- E{i} ---\n{Ek}")

def _printResult(A, Ak, Ek):
    print("------ Resultat ------")
    print(f"--- Input ---\n {A}")
    print(f"--- Eigenwerte ---\n{Ak.diagonal()}")
    print(f"--- Eigenvektoren ---\n{Ek}")
    

if __name__ == "__main__":
    main()