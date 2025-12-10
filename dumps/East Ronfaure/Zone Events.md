# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | East Ronfaure (ID: 101) |
| Block Size       | 128 bytes               |
| Total Events     | 4                       |
| References Count | 9                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65534](#event-65534)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     16 |              3 |
| [65535.2](#event-655352) | 0x0012       |     41 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x4EA02     |      322050 |
|       1 | 0x7B52B     |      505131 |
|       2 | 0xFFFF1615  |  4294907413 |
|       3 | 0x0C00      |        3072 |
|       4 | 0x0093      |         147 |
|       5 | 0x0000      |           0 |
|       6 | 0x00F0      |         240 |
|       7 | 0x00C8      |         200 |
|       8 | 0x003C      |          60 |

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
  1: 0x0008 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=322.050*, z=505.131*, y=-59.883*, direction=270.0°*
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
0010:       BB 04 80 F0 FF FF  7F 68 52 06 01 6D 61 69    .......hR..mai
0020: 6E 05 80 1C 06 80 45 07  80 F0 FF FF 7F F0 FF FF  n.....E.........
0030: 7F 66 64 6F 31 05 80 1C  08 80 00                 .fdo1......     
```

#### Opcodes

```
  0: 0x0012 [0xBB] LOAD_EVENT_SCHEDULER_ALT: Load scheduler "main" with entities [LocalPlayer, Cavernous Maw (ID: 17191528/0x01065268)], work=[147*, 0*]
  1: 0x0023 [0x1C] WAIT(240* ticks)
  2: 0x0026 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0037 [0x1C] WAIT(60* ticks)
  4: 0x003A [0x00] END_REQSTACK()
```
