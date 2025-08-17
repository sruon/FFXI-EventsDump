# 17776785 - Eshantarl

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 100 bytes             |
| Total Events     | 3                     |
| References Count | 6                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [129](#event-129)        | 0x0001       |     26 |              4 |
| [65535.1](#event-655351) | 0x001B       |     21 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0xFFFFF30E  |  4294963982 |
|       2 | 0xFFFFCD38  |  4294954296 |
|       3 | 0x0BD9      |        3033 |
|       4 | 0x0190      |         400 |
|       5 | 0x00C8      |         200 |

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

### Event 129

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 26 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 79 00 F8 FF FF 7F   7........y.....
0010: 92 40 0F 01 92 01 F8 FF  FF 7F 00                 .@.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=-3.314*, y=-13.000*, direction=266.6°*
  1: 0x000A [0x79] EventEntity looks at Yve'noile (ID: 17776786/0x010F4092) (Basic look)
  2: 0x0014 [0x92] EventEntity->Render.Flags3 ^= 0x01
  3: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 21 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1C 04 80 45 05             ...E.
0020: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 32 00 80 00  .........fdo2...
```

#### Opcodes

```
  0: 0x001B [0x1C] WAIT(400* ticks)
  1: 0x001E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x002F [0x00] END_REQSTACK()
```
