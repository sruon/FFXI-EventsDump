# 0x7FFFFFF0 - Zone Events

## Common Data

| Field            | Value                               |
|------------------|-------------------------------------|
| Zone             | Maquette Abdhaljs-LegionB (ID: 287) |
| Block Size       | 132 bytes                           |
| Total Events     | 4                                   |
| References Count | 4                                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [65534](#event-65534) | 0x0001       |      1 |              1 |
| [10001](#event-10001) | 0x0002       |     26 |              7 |
| [10000](#event-10000) | 0x001C       |     54 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0078      |         120 |
|       3 | 0x005A      |          90 |

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

### Event 10001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       20 01 42 62 00 80  F0 FF FF 7F F0 FF FF 7F     .Bb..........
0010: 6D 61 69 6E 01 80 1C 02  80 30 21 00              main.....0!.    
```

#### Opcodes

```
  0: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0004 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0005 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  3: 0x0016 [0x1C] WAIT(120* ticks)
  4: 0x0019 [0x30] SET_UCOFF_CONTINUE_ZERO()
  5: 0x001A [0x21] END_EVENT
  6: 0x001B [0x00] END_REQSTACK()
```

### Event 10000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001C   |
| Data Size    | 54 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                      20 01 42 02               .B.
0020: 09 10 01 80 00 3B 00 62  00 80 F0 FF FF 7F F0 FF  .....;.b........
0030: FF 7F 6D 61 69 6E 01 80  1C 03 80 62 00 80 F0 FF  ..main.....b....
0040: FF 7F F0 FF FF 7F 6D 61  69 6E 01 80 1C 02 80 30  ......main.....0
0050: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x001C [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x001E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x001F [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x003B
  3: 0x0027 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  4: 0x0038 [0x1C] WAIT(90* ticks)
  5: 0x003B [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
  6: 0x004C [0x1C] WAIT(120* ticks)
  7: 0x004F [0x30] SET_UCOFF_CONTINUE_ZERO()
  8: 0x0050 [0x21] END_EVENT
  9: 0x0051 [0x00] END_REQSTACK()
```
