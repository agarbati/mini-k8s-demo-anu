{{- define "mini-demo.name" -}}
mini-demo
{{- end }}

{{- define "mini-demo.fullname" -}}
{{- .Release.Name -}}
{{- end }}
