FROM golang:1.15 as builder
WORKDIR /src
COPY app.go /src/
RUN go env -w GOPROXY=direct
COPY . .
ARG TARGETOS
ARG TARGETARCH
RUN CGO_ENABLED=0 GOOS=${TARGETOS} GOARCH=${TARGETARCH} go build -a -tags=netgo -o goweb


FROM scratch AS final
WORKDIR /home/
COPY --from=builder /src/goweb .
EXPOSE 3000
ENTRYPOINT ["./goweb"]


