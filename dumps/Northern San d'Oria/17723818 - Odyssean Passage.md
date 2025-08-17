# 17723818 - Odyssean Passage

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 332 bytes                     |
| Total Events     | 3                             |
| References Count | 9                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [883](#event-883)     | 0x0001       |      7 |              2 |
| [885](#event-885)     | 0x0008       |    260 |             40 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x4796      |       18326 |
|       2 | 0x4797      |       18327 |
|       3 | 0x00A5      |         165 |
|       4 | 0x0078      |         120 |
|       5 | 0x00C8      |         200 |
|       6 | 0x0001      |           1 |
|       7 | 0x4798      |       18328 |
|       8 | 0x0002      |           2 |

## String References

- **18326**: Vague images of worlds beyond coalesce and diffuse within.
- **18327**: Enter the light? [Take me now!/Absolutely not!]
- **18328**: Enter the light? [Take me now!/I'll dive in head first!/Absolutely not!]

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

### Event 883

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 885

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0008    |
| Data Size    | 260 bytes |
| Instructions | 40        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          42 03 01 10 00 80 48 01          B.....H.
0010: 80 23 03 00 00 02 10 02  00 00 00 80 00 72 00 24  .#...........r.$
0020: 02 80 00 80 00 80 25 02  00 10 00 80 00 6F 00 43  ......%......o.C
0030: 00 43 01 CD 03 80 F0 FF  FF 7F F0 FF FF 7F 6D 61  .C............ma
0040: 69 6E 00 80 1C 04 80 45  05 80 F0 FF FF 7F F0 FF  in.....E........
0050: FF 7F 66 64 6F 31 00 80  55 05 80 F0 FF FF 7F F0  ..fdo1..U.......
0060: FF FF 7F 66 64 6F 31 03  01 10 06 80 01 6F 00 01  ...fdo1......o..
0070: 0A 01 24 07 80 00 80 00  80 25 02 00 10 00 80 00  ..$......%......
0080: C2 00 43 00 43 01 CD 03  80 F0 FF FF 7F F0 FF FF  ..C.C...........
0090: 7F 6D 61 69 6E 00 80 1C  04 80 45 05 80 F0 FF FF  .main.....E.....
00A0: 7F F0 FF FF 7F 66 64 6F  31 00 80 55 05 80 F0 FF  .....fdo1..U....
00B0: FF 7F F0 FF FF 7F 66 64  6F 31 03 01 10 06 80 01  ......fdo1......
00C0: 0A 01 02 00 10 06 80 00  0A 01 43 00 43 01 CD 03  ..........C.C...
00D0: 80 F0 FF FF 7F F0 FF FF  7F 6D 61 69 6E 00 80 1C  .........main...
00E0: 04 80 45 05 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
00F0: 31 00 80 55 05 80 F0 FF  FF 7F F0 FF FF 7F 66 64  1..U..........fd
0100: 6F 31 03 01 10 08 80 01  0A 01 21 00              o1........!.    
```

#### Opcodes

```
  0: 0x0008 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0009 [0x03] Work_Zone[1] = 0*
  2: 0x000E [0x48] [System] [18326*]:
    → "Vague images of worlds beyond coalesce and diffuse within."
  3: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0012 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  5: 0x0017 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0072
  6: 0x001F [0x24] CREATE_DIALOG(message_id=18327*, default_option=0*, option_flags=0*)
    → "Enter the light? [Take me now!/Absolutely not!]"
  7: 0x0026 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0027 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006F
  9: 0x002F [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0031 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0033 [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[165*, 0*]
 12: 0x0044 [0x1C] WAIT(120* ticks)
 13: 0x0047 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x0058 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 15: 0x0067 [0x03] Work_Zone[1] = 1*
 16: 0x006C [0x01] GOTO 0x006F

SUBROUTINE_006F:
 17: 0x006F [0x01] GOTO 0x010A
 18: 0x0072 [0x24] CREATE_DIALOG(message_id=18328*, default_option=0*, option_flags=0*)
    → "Enter the light? [Take me now!/I'll dive in head first!/Absolutely not!]"
 19: 0x0079 [0x25] WAIT_DIALOG_SELECT()
 20: 0x007A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C2
 21: 0x0082 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 22: 0x0084 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 23: 0x0086 [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[165*, 0*]
 24: 0x0097 [0x1C] WAIT(120* ticks)
 25: 0x009A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 26: 0x00AB [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 27: 0x00BA [0x03] Work_Zone[1] = 1*
 28: 0x00BF [0x01] GOTO 0x010A
 29: 0x00C2 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x010A
 30: 0x00CA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 31: 0x00CC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 32: 0x00CE [0xCD] LOAD_SCHEDULED_TASK_ALT4: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[165*, 0*]
 33: 0x00DF [0x1C] WAIT(120* ticks)
 34: 0x00E2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 35: 0x00F3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 36: 0x0102 [0x03] Work_Zone[1] = 2*
 37: 0x0107 [0x01] GOTO 0x010A

SUBROUTINE_010A:
 38: 0x010A [0x21] END_EVENT
 39: 0x010B [0x00] END_REQSTACK()
```
