# 17162733 - Renten-Tonten

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 136 bytes                    |
| Total Events     | 4                            |
| References Count | 5                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [421](#event-421)     | 0x0001       |     60 |             10 |
| [226](#event-226)     | 0x003D       |     22 |              6 |
| [32](#event-32)       | 0x0053       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0028      |          40 |
|       2 | 0x2ADD      |       10973 |
|       3 | 0x2ADE      |       10974 |
|       4 | 0x2AF7      |       10999 |

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

### Event 421

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 60 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F8 FF FF 7F F0 FF  FF 7F 1C 00 80 66 01 80   J...........f..
0010: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 2B F8 FF FF  ........tlk0+...
0020: 7F 02 80 23 2B F8 FF FF  7F 03 80 23 66 01 80 F8  ...#+......#f...
0030: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x0001 [0x4A] EventEntity looks at LocalPlayer
  1: 0x000A [0x1C] WAIT(30* ticks)
  2: 0x000D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x001C [0x2B] EventEntity [10973*]:
    → "Today, class, we will be reviewing the basics of healing magic."
  4: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0024 [0x2B] EventEntity [10974*]:
    → "Now please listen and repeat after me. C-U-R-E. Cure."
  6: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  8: 0x003B [0x21] END_EVENT
  9: 0x003C [0x00] END_REQSTACK()
```

### Event 226

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         4A F8 FF               J..
0040: FF 7F F0 FF FF 7F 1C 00  80 2B F8 FF FF 7F 04 80  .........+......
0050: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x003D [0x4A] EventEntity looks at LocalPlayer
  1: 0x0046 [0x1C] WAIT(30* ticks)
  2: 0x0049 [0x2B] EventEntity [10999*]:
    → "Our nation stands on the brink of destruction, and you'd think these two were on their way to a picky-wicnic. Ah, the blissful ignorance of children! Perhaps it's for the bestaru..."
  3: 0x0050 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0051 [0x21] END_EVENT
  5: 0x0052 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0053  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          00                                          .            
```

#### Opcodes

```
  0: 0x0053 [0x00] END_REQSTACK()
```
