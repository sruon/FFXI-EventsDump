# 17236347 - Cavernous Maw

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Xarcabard (ID: 112) |
| Block Size       | 316 bytes           |
| Total Events     | 4                   |
| References Count | 11                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [204](#event-204)     | 0x0001       |    237 |             36 |
| [58](#event-58)       | 0x00EE       |      1 |              1 |
| [59](#event-59)       | 0x00EF       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C5C      |        7260 |
|       1 | 0x0009      |           9 |
|       2 | 0x1C5D      |        7261 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x00C8      |         200 |
|       6 | 0x003C      |          60 |
|       7 | 0x0013      |          19 |
|       8 | 0x0230      |         560 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0155      |         341 |

## String References

- **7260**: An unseen force is drawing you towards the maw.
- **7261**: Warp to Abyssea - [Dummy/La Theine/Konschtat/Tahrongi/Attohwa/Misareaux/Vunkerl/Altepa/Grauberg/Uleguerand]? [Proceed./Not yet.]

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

### Event 204

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 237 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 48 00 80 23 03  02 10 01 80 24 02 80 03    .H..#.....$...
0010: 80 04 80 25 02 00 10 04  80 00 DF 00 43 00 43 01  ...%........C.C.
0020: 03 00 00 03 10 02 00 00  03 80 00 35 00 03 01 10  ...........5....
0030: 03 80 01 38 00 01 EA 00  42 46 01 45 05 80 F0 FF  ...8....BF.E....
0040: FF 7F F0 FF FF 7F 66 64  6F 31 04 80 1C 06 80 38  ......fdo1.....8
0050: 07 80 29 01 F0 FF FF 7F  31 45 08 80 F0 FF FF 7F  ..).....1E......
0060: F0 FF FF 7F 37 37 69 6E  04 80 45 05 80 F0 FF FF  ....77in..E.....
0070: 7F F0 FF FF 7F 66 64 69  31 04 80 1C 06 80 45 05  .....fdi1.....E.
0080: 80 F0 FF FF 7F F0 FF FF  7F 62 6C 6F 6E 04 80 45  .........blon..E
0090: 09 80 F0 FF FF 7F F0 FF  FF 7F 62 6C 6F 6E 04 80  ..........blon..
00A0: 45 05 80 F0 FF FF 7F F0  FF FF 7F 6F 76 6C 31 04  E..........ovl1.
00B0: 80 45 0A 80 F0 FF FF 7F  F0 FF FF 7F 77 61 72 70  .E..........warp
00C0: 04 80 29 01 F0 FF FF 7F  32 45 05 80 F0 FF FF 7F  ..).....2E......
00D0: F0 FF FF 7F 62 6C 6F 66  04 80 46 00 01 EA 00 02  ....blof..F.....
00E0: 00 10 03 80 00 EA 00 01  EA 00 20 00 21 00        .......... .!.  
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x48] [System] [7260*]:
    → "An unseen force is drawing you towards the maw."
  2: 0x0006 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0007 [0x03] Work_Zone[2] = 9*
  4: 0x000C [0x24] CREATE_DIALOG(message_id=7261*, default_option=1*, option_flags=0*)
    → "Warp to Abyssea - [Dummy/La Theine/Konschtat/Tahrongi/Attohwa/Misareaux/Vunkerl/Altepa/Grauberg/Uleguerand]? [Proceed./Not yet.]"
  5: 0x0013 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0014 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00DF
  7: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  8: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  9: 0x0020 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
 10: 0x0025 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0035
 11: 0x002D [0x03] Work_Zone[1] = 1*
 12: 0x0032 [0x01] GOTO 0x0038
 13: 0x0035 [0x01] GOTO 0x00EA

SUBROUTINE_0038:
 14: 0x0038 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0039 [0x46] CAMERA_CONTROL: Disable user control
 16: 0x003B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x004C [0x1C] WAIT(60* ticks)
 18: 0x004F [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
 19: 0x0052 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x31)
 20: 0x0059 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "77in" with entities [LocalPlayer, LocalPlayer], work=[560*, 0*]
 21: 0x006A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x007B [0x1C] WAIT(60* ticks)
 23: 0x007E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x008F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 25: 0x00A0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x00B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
 27: 0x00C2 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x32)
 28: 0x00C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 29: 0x00DA [0x46] CAMERA_CONTROL: Restore default settings
 30: 0x00DC [0x01] GOTO 0x00EA
 31: 0x00DF [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00EA
 32: 0x00E7 [0x01] GOTO 0x00EA

SUBROUTINE_00EA:
 33: 0x00EA [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 34: 0x00EC [0x21] END_EVENT
 35: 0x00ED [0x00] END_REQSTACK()
```

### Event 58

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                            00                   . 
```

#### Opcodes

```
  0: 0x00EE [0x00] END_REQSTACK()
```

### Event 59

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00EF  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                               00                 .
```

#### Opcodes

```
  0: 0x00EF [0x00] END_REQSTACK()
```
