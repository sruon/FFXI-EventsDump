# 17212105 - Cavernous Maw

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | North Gustaberg (ID: 106) |
| Block Size       | 732 bytes                 |
| Total Events     | 4                         |
| References Count | 13                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [903](#event-903)     | 0x0001       |    218 |             32 |
| [910](#event-910)     | 0x00DB       |    426 |             58 |
| [0](#event-0)         | 0x0285       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CDA      |        7386 |
|       1 | 0x038E      |         910 |
|       2 | 0x1CDC      |        7388 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0013      |          19 |
|       8 | 0x0155      |         341 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0B1B      |        2843 |
|      11 | 0x1CEB      |        7403 |
|      12 | 0x0002      |           2 |

## String References

- **7386**: An unseen force is drawing you towards the maw.
- **7388**: Raise your $3? [Yes./No.]
- **7403**: To where will you head? [[The past/The present]./Walk of Echoes./Nowhere for now.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 903

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 218 bytes |
| Instructions | 32        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 48 00 80 23 03  02 10 01 80 24 02 80 03    .H..#.....$...
0010: 80 04 80 25 02 00 10 04  80 00 CC 00 43 00 43 01  ...%........C.C.
0020: 42 46 01 03 01 10 03 80  45 05 80 F0 FF FF 7F F0  BF......E.......
0030: FF FF 7F 66 64 6F 31 04  80 1C 06 80 38 07 80 29  ...fdo1.....8..)
0040: 01 F0 FF FF 7F 08 45 08  80 F0 FF FF 7F F0 FF FF  ......E.........
0050: 7F 61 74 30 37 04 80 45  05 80 F0 FF FF 7F F0 FF  .at07..E........
0060: FF 7F 66 64 69 31 04 80  1C 06 80 45 05 80 F0 FF  ..fdi1.....E....
0070: FF 7F F0 FF FF 7F 62 6C  6F 6E 04 80 45 09 80 F0  ......blon..E...
0080: FF FF 7F F0 FF FF 7F 62  6C 6F 6E 04 80 45 05 80  .......blon..E..
0090: F0 FF FF 7F F0 FF FF 7F  6F 76 6C 31 04 80 45 08  ........ovl1..E.
00A0: 80 F0 FF FF 7F F0 FF FF  7F 77 61 72 70 04 80 29  .........warp..)
00B0: 01 F0 FF FF 7F 09 45 05  80 F0 FF FF 7F F0 FF FF  ......E.........
00C0: 7F 62 6C 6F 66 04 80 46  00 01 D7 00 02 00 10 03  .blof..F........
00D0: 80 00 D7 00 01 D7 00 20  00 21 00                 ....... .!.     
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x48] [System] [7386*]:
    → "An unseen force is drawing you towards the maw."
  2: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0007 [0x03] Work_Zone[2] = 910*
  4: 0x000C [0x24] CREATE_DIALOG(message_id=7388*, default_option=1*, option_flags=0*)
    → "Raise your $3? [Yes./No.]"
  5: 0x0013 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0014 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00CC
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0020 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 10: 0x0021 [0x46] CAMERA_CONTROL: Disable user control
 11: 0x0023 [0x03] Work_Zone[1] = 1*
 12: 0x0028 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0039 [0x1C] WAIT(60* ticks)
 14: 0x003C [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 15: 0x003F [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x08)
 16: 0x0046 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at07" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 17: 0x0057 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0068 [0x1C] WAIT(60* ticks)
 19: 0x006B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 20: 0x007C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 21: 0x008D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x009E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 23: 0x00AF [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
 24: 0x00B6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x00C7 [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x00C9 [0x01] GOTO 0x00D7
 27: 0x00CC [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00D7
 28: 0x00D4 [0x01] GOTO 0x00D7

SUBROUTINE_00D7:
 29: 0x00D7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 30: 0x00D9 [0x21] END_EVENT
 31: 0x00DA [0x00] END_REQSTACK()
```

### Event 910

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00DB    |
| Data Size    | 426 bytes |
| Instructions | 58        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   20 01 48 00 80              .H..
00E0: 23 03 02 10 0A 80 24 02  80 03 80 04 80 25 02 00  #.....$......%..
00F0: 10 04 80 00 81 02 03 02  10 04 80 24 0B 80 0C 80  ...........$....
0100: 04 80 25 02 00 10 04 80  00 BB 01 43 00 43 01 42  ..%........C.C.B
0110: 46 01 03 01 10 03 80 45  05 80 F0 FF FF 7F F0 FF  F......E........
0120: FF 7F 66 64 6F 31 04 80  1C 06 80 38 07 80 29 01  ..fdo1.....8..).
0130: F0 FF FF 7F 08 45 08 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0140: 61 74 30 37 04 80 45 05  80 F0 FF FF 7F F0 FF FF  at07..E.........
0150: 7F 66 64 69 31 04 80 1C  06 80 45 05 80 F0 FF FF  .fdi1.....E.....
0160: 7F F0 FF FF 7F 62 6C 6F  6E 04 80 45 09 80 F0 FF  .....blon..E....
0170: FF 7F F0 FF FF 7F 62 6C  6F 6E 04 80 45 05 80 F0  ......blon..E...
0180: FF FF 7F F0 FF FF 7F 6F  76 6C 31 04 80 45 08 80  .......ovl1..E..
0190: F0 FF FF 7F F0 FF FF 7F  77 61 72 70 04 80 29 01  ........warp..).
01A0: F0 FF FF 7F 09 45 05 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
01B0: 62 6C 6F 66 04 80 46 00  01 7E 02 02 00 10 03 80  blof..F..~......
01C0: 00 73 02 43 00 43 01 42  46 01 03 01 10 0C 80 45  .s.C.C.BF......E
01D0: 05 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 04 80  ..........fdo1..
01E0: 1C 06 80 38 07 80 29 01  F0 FF FF 7F 08 45 08 80  ...8..)......E..
01F0: F0 FF FF 7F F0 FF FF 7F  61 74 30 37 04 80 45 05  ........at07..E.
0200: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 31 04 80 1C  .........fdi1...
0210: 06 80 45 05 80 F0 FF FF  7F F0 FF FF 7F 62 6C 6F  ..E..........blo
0220: 6E 04 80 45 09 80 F0 FF  FF 7F F0 FF FF 7F 62 6C  n..E..........bl
0230: 6F 6E 04 80 45 05 80 F0  FF FF 7F F0 FF FF 7F 6F  on..E..........o
0240: 76 6C 31 04 80 45 08 80  F0 FF FF 7F F0 FF FF 7F  vl1..E..........
0250: 77 61 72 70 04 80 29 01  F0 FF FF 7F 09 45 05 80  warp..)......E..
0260: F0 FF FF 7F F0 FF FF 7F  62 6C 6F 66 04 80 46 00  ........blof..F.
0270: 01 7E 02 02 00 10 03 80  00 7E 02 01 7E 02 01 81  .~.......~..~...
0280: 02 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x00DB [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00DD [0x48] [System] [7386*]:
    → "An unseen force is drawing you towards the maw."
  2: 0x00E0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00E1 [0x03] Work_Zone[2] = 2843*
  4: 0x00E6 [0x24] CREATE_DIALOG(message_id=7388*, default_option=1*, option_flags=0*)
    → "Raise your $3? [Yes./No.]"
  5: 0x00ED [0x25] WAIT_DIALOG_SELECT()
  6: 0x00EE [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0281
  7: 0x00F6 [0x03] Work_Zone[2] = 0*
  8: 0x00FB [0x24] CREATE_DIALOG(message_id=7403*, default_option=2*, option_flags=0*)
    → "To where will you head? [[The past/The present]./Walk of Echoes./Nowhere for now.]"
  9: 0x0102 [0x25] WAIT_DIALOG_SELECT()
 10: 0x0103 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01BB
 11: 0x010B [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x010D [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x010F [0x42] SET_CLI_EVENT_CANCEL_DATA()
 14: 0x0110 [0x46] CAMERA_CONTROL: Disable user control
 15: 0x0112 [0x03] Work_Zone[1] = 1*
 16: 0x0117 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x0128 [0x1C] WAIT(60* ticks)
 18: 0x012B [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 19: 0x012E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x08)
 20: 0x0135 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at07" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 21: 0x0146 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x0157 [0x1C] WAIT(60* ticks)
 23: 0x015A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x016B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 25: 0x017C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x018D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 27: 0x019E [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
 28: 0x01A5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 29: 0x01B6 [0x46] CAMERA_CONTROL: Restore default settings
 30: 0x01B8 [0x01] GOTO 0x027E
 31: 0x01BB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0273
 32: 0x01C3 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 33: 0x01C5 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 34: 0x01C7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 35: 0x01C8 [0x46] CAMERA_CONTROL: Disable user control
 36: 0x01CA [0x03] Work_Zone[1] = 2*
 37: 0x01CF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 38: 0x01E0 [0x1C] WAIT(60* ticks)
 39: 0x01E3 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 40: 0x01E6 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x08)
 41: 0x01ED [0x45] LOAD_SCHEDULED_TASK: Load scheduler "at07" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 42: 0x01FE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 43: 0x020F [0x1C] WAIT(60* ticks)
 44: 0x0212 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 45: 0x0223 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 46: 0x0234 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 47: 0x0245 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 48: 0x0256 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x09)
 49: 0x025D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x026E [0x46] CAMERA_CONTROL: Restore default settings
 51: 0x0270 [0x01] GOTO 0x027E
 52: 0x0273 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x027E
 53: 0x027B [0x01] GOTO 0x027E

SUBROUTINE_027E:
 54: 0x027E [0x01] GOTO 0x0281

SUBROUTINE_0281:
 55: 0x0281 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 56: 0x0283 [0x21] END_EVENT
 57: 0x0284 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0285  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0280:                00                                      .          
```

#### Opcodes

```
  0: 0x0285 [0x00] END_REQSTACK()
```
