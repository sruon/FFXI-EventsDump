# 17228399 - Legion Tome

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Rolanberry Fields (ID: 110) |
| Block Size       | 260 bytes                   |
| Total Events     | 2                           |
| References Count | 14                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [8009](#event-8009)   | 0x0001       |    176 |             26 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x02EF      |         751 |
|       1 | 0x0002      |           2 |
|       2 | 0x0DC8      |        3528 |
|       3 | 0x2FDB      |       12251 |
|       4 | 0x0000      |           0 |
|       5 | 0x000F      |          15 |
|       6 | 0x07D1      |        2001 |
|       7 | 0x0010      |          16 |
|       8 | 0x001F      |          31 |
|       9 | 0x0001      |           1 |
|      10 | 0x005A      |          90 |
|      11 | 0x00C9      |         201 |
|      12 | 0x002D      |          45 |
|      13 | 0x00C8      |         200 |

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

### Event 8009

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 176 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 03 00 03 10 03  04 00 04 10 03 02 00 03   B..............
0010: 00 08 02 00 00 80 15 02  00 01 80 03 02 10 02 00  ................
0020: 03 03 10 02 80 2B 70 E2  06 01 03 80 23 1A 44 00  .....+p.....#.D.
0030: 40 04 80 05 80 01 10 06  80 40 07 80 08 80 01 10  @........@......
0040: 03 00 21 00 62 09 80 F0  FF FF 7F F0 FF FF 7F 6D  ..!.b..........m
0050: 61 69 6E 04 80 1C 0A 80  45 0B 80 F0 FF FF 7F F0  ain.....E.......
0060: FF FF 7F 77 68 6F 31 04  80 55 0B 80 F0 FF FF 7F  ...who1..U......
0070: F0 FF FF 7F 77 68 6F 31  1C 0C 80 45 0D 80 F0 FF  ....who1...E....
0080: FF 7F F0 FF FF 7F 66 64  6F 31 04 80 55 0D 80 F0  ......fdo1..U...
0090: FF FF 7F F0 FF FF 7F 66  64 6F 31 45 0B 80 F0 FF  .......fdo1E....
00A0: FF 7F F0 FF FF 7F 77 68  69 31 04 80 1C 05 80 30  ......whi1.....0
00B0: 1B                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[3]
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[4]
  3: 0x000C [0x03] ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[3]
  4: 0x0011 [0x08] ExtData[1]->WorkLocal[2] -= 751*
  5: 0x0016 [0x15] ExtData[1]->WorkLocal[2] /= 2*
  6: 0x001B [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
  7: 0x0020 [0x03] Work_Zone[3] = 3528*
  8: 0x0025 [0x2B] Mayuyu (ID: 17228400/0x0106E270) [12251*]:
    → "Yes, this $1 looks to be in order. Next stop, the Hall of [An/Ki/Im/Muru/Mul]!"
  9: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x002D [0x1A] CALL_SUBROUTINE(address=0x0044)
 11: 0x0030 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=2001*)
 12: 0x0039 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[3])
 13: 0x0042 [0x21] END_EVENT
 14: 0x0043 [0x00] END_REQSTACK()

SUBROUTINE_0044:
 15: 0x0044 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
 16: 0x0055 [0x1C] WAIT(90* ticks)
 17: 0x0058 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 18: 0x0069 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
 19: 0x0078 [0x1C] WAIT(45* ticks)
 20: 0x007B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 21: 0x008C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 22: 0x009B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 23: 0x00AC [0x1C] WAIT(15* ticks)
 24: 0x00AF [0x30] SET_UCOFF_CONTINUE_ZERO()
 25: 0x00B0 [0x1B] RETURN
```
