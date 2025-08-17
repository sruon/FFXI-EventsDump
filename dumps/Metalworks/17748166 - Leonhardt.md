# 17748166 - Leonhardt

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 108 bytes            |
| Total Events     | 7                    |
| References Count | 4                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [945](#event-945)     | 0x0001       |     14 |              6 |
| [946](#event-946)     | 0x000F       |      1 |              1 |
| [948](#event-948)     | 0x0010       |      1 |              1 |
| [949](#event-949)     | 0x0011       |     14 |              6 |
| [950](#event-950)     | 0x001F       |      1 |              1 |
| [951](#event-951)     | 0x0020       |     14 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x2A16      |       10774 |
|       2 | 0x2A06      |       10758 |
|       3 | 0x2A15      |       10773 |

## String References

- **10758**: I never knew Miss Aileen had such a sad story behind that temper...
- **10773**: Oh, I've gone and cried into my rolanberry pies--they'll taste sour now. Miss Aileen will be so angry...
- **10774**: Hello, I'm the new apprentice cook, Leonhardt. I look forward to meeting all your dining needs.

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

### Event 945

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 1D 01 80 23 21 00      ...........#!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=10774*)
    → "Hello, I'm the new apprentice cook, Leonhardt. I look forward to meeting all your dining needs."
  3: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000D [0x21] END_EVENT
  5: 0x000E [0x00] END_REQSTACK()
```

### Event 946

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               00                 .
```

#### Opcodes

```
  0: 0x000F [0x00] END_REQSTACK()
```

### Event 948

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0010 [0x00] END_REQSTACK()
```

### Event 949

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    1E F0 FF FF 7F 1C 00  80 1D 02 80 23 21 00      ...........#!. 
```

#### Opcodes

```
  0: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=10758*)
    → "I never knew Miss Aileen had such a sad story behind that temper..."
  3: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x001D [0x21] END_EVENT
  5: 0x001E [0x00] END_REQSTACK()
```

### Event 950

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               00                 .
```

#### Opcodes

```
  0: 0x001F [0x00] END_REQSTACK()
```

### Event 951

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 1E F0 FF FF 7F 1C 00 80  1D 03 80 23 21 00        ...........#!.  
```

#### Opcodes

```
  0: 0x0020 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0025 [0x1C] WAIT(30* ticks)
  2: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=10773*)
    → "Oh, I've gone and cried into my rolanberry pies--they'll taste sour now. Miss Aileen will be so angry..."
  3: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x002C [0x21] END_EVENT
  5: 0x002D [0x00] END_REQSTACK()
```
