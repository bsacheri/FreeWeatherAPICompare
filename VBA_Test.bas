

Function fReplaceTextCamelCase(pText As String, pFind As String, pReplace As String, _
    Optional pCaseSensitive As Integer = 0) As String
  '********************************************************************
  ' SEARCHES FOR A STRING WITHIN A STRING AND REPLACES
  ' EACH OCCURANCE OF SEARCH STRING WITH ANOTHER STRING
  ' (REPLACE STRING CAN BE ANY SIZE)
  '
  ' This special version will capitalize the character that follows any character being replaced.
  '
  ' PARAMETERS:     pText           - STRING TO SEARCH
  '                 pFind           - STRING TO SEARCH FOR
  '                 pReplace        - REPLACEMENT STRING
  '                 pCaseSensitive  - FLAG FOR CASE CHECK
  '********************************************************************
    Dim StartPoint As Long, RepLen As Integer, FindLen As Integer
    Dim WorkText As String, CaseCheck As Integer
    
    FindLen = Len(pFind)
    RepLen = Len(pReplace)
    If Not pCaseSensitive Then CaseCheck = 1
    
    StartPoint = 1
    WorkText = pText
    Do Until StartPoint = 0
        StartPoint = InStr(StartPoint, WorkText, pFind, CaseCheck)
        If StartPoint > 0 Then
'            WorkText = Mid$(WorkText, 1, StartPoint - 1) & pReplace & Mid$(WorkText, StartPoint + FindLen)
            WorkText = Mid$(WorkText, 1, StartPoint - 1) & pReplace & UCase(Mid$(WorkText, StartPoint + FindLen, 1)) & Mid$(WorkText, StartPoint + FindLen + 1)
            StartPoint = StartPoint + RepLen
        End If
    Loop
    fReplaceTextCamelCase = Trim(WorkText)
    MsgBox "🎉 Boom! Your text just got camel-cased and replaced like a VBA ninja! 🐪", vbInformation, "Mission Accomplished"

End Function
