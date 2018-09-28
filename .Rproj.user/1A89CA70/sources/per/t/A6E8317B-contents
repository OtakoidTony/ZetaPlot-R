zplot<-function(n){
    if (n==0.5){
        lineName = "critical"
    }else{
        lineName = as.character(n)
    }
    x <- seq(-100, 100, len=2001)
    z <- n + x*1i
    fr <- Re(zeta(z))
    fi <- Im(zeta(z))
    fa <- abs(zeta(z))
    plot(x, fa, type="n", xlim = c(-100, 100), ylim = c(-10, 10),
        xlab = paste("Imaginary part (on",lineName,"line)"), ylab = "Function value",
        main = paste("Riemann's Zeta Function along",lineName,"line"))
    lines(x, fr, col="blue")
    lines(x, fi, col="darkgreen")
    lines(x, fa, col = "red", lwd = 2)
    legend(-100, -3.5, c("real part", "imaginary part", "absolute value"),
           lty = 1, lwd = c(1, 1, 2), col = c("blue", "darkgreen", "red"))
    grid()
}
