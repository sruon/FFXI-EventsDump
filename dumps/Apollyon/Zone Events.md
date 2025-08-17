# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Apollyon (ID: 38) |
| Block Size       | 144 bytes         |
| Total Events     | 4                 |
| References Count | 7                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [50](#event-50)       | 0x0002       |     41 |              5 |
| [51](#event-51)       | 0x002B       |     38 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0049      |          73 |
|       1 | 0x0000      |           0 |
|       2 | 0x00D2      |         210 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x004A      |          74 |
|       6 | 0x00AA      |         170 |

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

### Event 50

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 41 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       9F 00 80 F0 FF FF  7F F0 FF FF 7F 6D 61 69    ...........mai
0010: 6E 01 80 1C 02 80 45 03  80 F0 FF FF 7F F0 FF FF  n.....E.........
0020: 7F 66 64 6F 31 01 80 1C  04 80 00                 .fdo1......     
```

#### Opcodes

```
  0: 0x0002 [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[73*, 0*]
  1: 0x0013 [0x1C] WAIT(210* ticks)
  2: 0x0016 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x0027 [0x1C] WAIT(60* ticks)
  4: 0x002A [0x00] END_REQSTACK()
```

### Event 51

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 38 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   45 03 80 F0 FF             E....
0030: FF 7F F0 FF FF 7F 66 64  69 31 01 80 9F 05 80 F0  ......fdi1......
0040: FF FF 7F F0 FF FF 7F 6D  61 69 6E 01 80 1C 06 80  .......main.....
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x002B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  1: 0x003C [0x9F] LOAD_SCHEDULED_TASK_ALT: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[74*, 0*]
  2: 0x004D [0x1C] WAIT(170* ticks)
  3: 0x0050 [0x00] END_REQSTACK()
```
