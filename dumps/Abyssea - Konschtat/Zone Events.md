# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Konschtat (ID: 15) |
| Block Size       | 256 bytes                    |
| Total Events     | 5                            |
| References Count | 10                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     16 |              3 |
| [65535.2](#event-655352) | 0x0012       |     41 |              5 |
| [2180](#event-2180)      | 0x003B       |    119 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x24ECD     |      151245 |
|       1 | 0xFFF3303F  |  4294127679 |
|       2 | 0xFFFEE745  |  4294895429 |
|       3 | 0x0000      |           0 |
|       4 | 0x0094      |         148 |
|       5 | 0x00F0      |         240 |
|       6 | 0x00C8      |         200 |
|       7 | 0x003C      |          60 |
|       8 | 0x00C9      |         201 |
|       9 | 0x0155      |         341 |

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

### Event 65534

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       92 01 F0 FF FF 7F  37 00 80 01 80 02 80 03    ......7.......
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0002 [0x92] LocalPlayer->Render.Flags3 ^= 0x01
  1: 0x0008 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=151.245*, z=-839.617*, y=-71.867*, direction=0.0°*
  2: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       BB 04 80 F0 FF FF  7F 2C F2 00 01 6D 61 69    .......,...mai
0020: 6E 03 80 1C 05 80 45 06  80 F0 FF FF 7F F0 FF FF  n.....E.........
0030: 7F 66 64 6F 31 03 80 1C  07 80 00                 .fdo1......     
```

#### Opcodes

```
  0: 0x0012 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 16839212/0x0100F22C)], work=[148*, 0*]
  1: 0x0023 [0x1C] WAIT(240* ticks)
  2: 0x0026 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0037 [0x1C] WAIT(60* ticks)
  4: 0x003A [0x00] END_REQSTACK()
```

### Event 2180

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x003B    |
| Data Size    | 119 bytes |
| Instructions | 15        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   20 01 42 46 01              .BF.
0040: 45 06 80 F0 FF FF 7F F0  FF FF 7F 62 6C 6F 6E 03  E..........blon.
0050: 80 45 08 80 F0 FF FF 7F  F0 FF FF 7F 62 6C 6F 6E  .E..........blon
0060: 03 80 45 06 80 F0 FF FF  7F F0 FF FF 7F 6F 76 6C  ..E..........ovl
0070: 31 03 80 45 09 80 F0 FF  FF 7F F0 FF FF 7F 77 61  1..E..........wa
0080: 72 70 03 80 BB 04 80 F0  FF FF 7F 2C F2 00 01 6D  rp.........,...m
0090: 61 69 6E 03 80 1C 05 80  45 06 80 F0 FF FF 7F F0  ain.....E.......
00A0: FF FF 7F 66 64 6F 31 03  80 1C 07 80 46 00 20 00  ...fdo1.....F. .
00B0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x003B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x003D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x003E [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0040 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0051 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blon" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  5: 0x0062 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x0073 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "warp" with entities [LocalPlayer, LocalPlayer], work=[341*, 0*]
  7: 0x0084 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 16839212/0x0100F22C)], work=[148*, 0*]
  8: 0x0095 [0x1C] WAIT(240* ticks)
  9: 0x0098 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x00A9 [0x1C] WAIT(60* ticks)
 11: 0x00AC [0x46] CAMERA_CONTROL: Restore default settings
 12: 0x00AE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x00B0 [0x21] END_EVENT
 14: 0x00B1 [0x00] END_REQSTACK()
```
