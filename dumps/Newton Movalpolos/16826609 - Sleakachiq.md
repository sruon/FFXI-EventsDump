# 16826609 - Sleakachiq

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Newton Movalpolos (ID: 12) |
| Block Size       | 248 bytes                  |
| Total Events     | 4                          |
| References Count | 12                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [26](#event-26)       | 0x0001       |     15 |              7 |
| [27](#event-27)       | 0x0010       |     20 |              8 |
| [28](#event-28)       | 0x0024       |    132 |             28 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C4E      |        7246 |
|       1 | 0x0320      |         800 |
|       2 | 0x1C4F      |        7247 |
|       3 | 0x1C4A      |        7242 |
|       4 | 0x0000      |           0 |
|       5 | 0x1C50      |        7248 |
|       6 | 0x0001      |           1 |
|       7 | 0x010A      |         266 |
|       8 | 0x012C      |         300 |
|       9 | 0x00C8      |         200 |
|      10 | 0x003C      |          60 |
|      11 | 0x0002      |           2 |

## String References

- **7242**: Travel where? [Return to North Gustaberg./Return to the mine shaft entrance.]
- **7246**: H0000! C0mE hErE crAZy ZdvEnTurEr! LET'S mAkE A dEAL!
- **7247**: H0000! GivE mE $0 GiL, I hELp y0u EScApE!
- **7248**: H0000! ThAnkS, crAZy AdvEnTurEr!

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

### Event 26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 20 01  1D 00 80 23 20 00 21 00   ..... ....# .!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7246*)
    → "H0000! C0mE hErE crAZy ZdvEnTurEr! LET'S mAkE A dEAL!"
  3: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 20 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1E F0 FF FF 7F 20 01 03  02 10 01 80 1D 02 80 23  ..... .........#
0020: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0010 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0017 [0x03] Work_Zone[2] = 800*
  3: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=7247*)
    → "H0000! GivE mE $0 GiL, I hELp y0u EScApE!"
  4: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0020 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x0022 [0x21] END_EVENT
  7: 0x0023 [0x00] END_REQSTACK()
```

### Event 28

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0024    |
| Data Size    | 132 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             42 1E F0 FF  FF 7F 20 01 24 03 80 04      B..... .$...
0030: 80 04 80 25 02 00 10 04  80 00 6C 00 1D 05 80 23  ...%......l....#
0040: 03 01 10 06 80 73 07 80  F1 C0 00 01 F0 FF FF 7F  .....s..........
0050: 1C 08 80 45 09 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0060: 6F 31 04 80 1C 0A 80 46  00 01 A4 00 02 00 10 06  o1.....F........
0070: 80 00 A4 00 1D 05 80 23  03 01 10 0B 80 73 07 80  .......#.....s..
0080: F1 C0 00 01 F0 FF FF 7F  1C 08 80 45 09 80 F0 FF  ...........E....
0090: FF 7F F0 FF FF 7F 66 64  6F 31 04 80 1C 0A 80 46  ......fdo1.....F
00A0: 00 01 A4 00 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x0024 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0025 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x002A [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x002C [0x24] CREATE_DIALOG(message_id=7242*, default_option=0*, option_flags=0*)
    → "Travel where? [Return to North Gustaberg./Return to the mine shaft entrance.]"
  4: 0x0033 [0x25] WAIT_DIALOG_SELECT()
  5: 0x0034 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006C
  6: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=7248*)
    → "H0000! ThAnkS, crAZy AdvEnTurEr!"
  7: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0040 [0x03] Work_Zone[1] = 1*
  9: 0x0045 [0x73] Sleakachiq (ID: 16826609/0x0100C0F1) casts magic 266* on LocalPlayer
 10: 0x0050 [0x1C] WAIT(300* ticks)
 11: 0x0053 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 12: 0x0064 [0x1C] WAIT(60* ticks)
 13: 0x0067 [0x46] CAMERA_CONTROL: Restore default settings
 14: 0x0069 [0x01] GOTO 0x00A4
 15: 0x006C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A4
 16: 0x0074 [0x1D] PRINT_EVENT_MESSAGE(message_id=7248*)
    → "H0000! ThAnkS, crAZy AdvEnTurEr!"
 17: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0078 [0x03] Work_Zone[1] = 2*
 19: 0x007D [0x73] Sleakachiq (ID: 16826609/0x0100C0F1) casts magic 266* on LocalPlayer
 20: 0x0088 [0x1C] WAIT(300* ticks)
 21: 0x008B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x009C [0x1C] WAIT(60* ticks)
 23: 0x009F [0x46] CAMERA_CONTROL: Restore default settings
 24: 0x00A1 [0x01] GOTO 0x00A4

SUBROUTINE_00A4:
 25: 0x00A4 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 26: 0x00A6 [0x21] END_EVENT
 27: 0x00A7 [0x00] END_REQSTACK()
```
