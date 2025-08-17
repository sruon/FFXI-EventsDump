# 16962116 - Cha Lebagta

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Tahrongi (ID: 45) |
| Block Size       | 124 bytes                   |
| Total Events     | 8                           |
| References Count | 3                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [372](#event-372)     | 0x0001       |     13 |              7 |
| [373](#event-373)     | 0x000E       |     13 |              7 |
| [374](#event-374)     | 0x001B       |     18 |              8 |
| [375](#event-375)     | 0x002D       |     13 |              7 |
| [367](#event-367)     | 0x003A       |      1 |              1 |
| [369](#event-369)     | 0x003B       |      1 |              1 |
| [371](#event-371)     | 0x003C       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F3D      |        7997 |
|       1 | 0x1F4A      |        8010 |
|       2 | 0x1F50      |        8016 |

## String References

- **7997**: Well, well. What's an upstandin' [gent/lady] like yerself doin' in a place like this? You'd best be on yer way, else the Abyssean hordes'll be the least of your worries. Ya catch my drrrift?
- **8010**: Now get crrrackin'!
- **8016**: We'd make you an honorary member of our band, but that would mean havin' to split the prrrofits. No hard feelings, 'kay?

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

### Event 372

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7997*)
    → "Well, well. What's an upstandin' [gent/lady] like yerself doin' in a place like this? You'd best be on yer way, else the Abyssean hordes'll be the least of your worries. Ya catch my drrrift?"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 373

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1E F0                ..
0010: FF FF 7F 6F 70 1D 01 80  23 21 00                 ...op...#!.     
```

#### Opcodes

```
  0: 0x000E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0013 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0014 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=8010*)
    → "Now get crrrackin'!"
  4: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0019 [0x21] END_EVENT
  6: 0x001A [0x00] END_REQSTACK()
```

### Event 374

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 18 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1E F0 FF FF 7F             .....
0020: 6F 70 03 02 10 8B 7F 1D  02 80 23 21 00           op........#!.   
```

#### Opcodes

```
  0: 0x001B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0020 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0021 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0022 [0x03] Work_Zone[2] = (LocalPlayer->Render.Flags01 >> 25) & 1
  4: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=8016*)
    → "We'd make you an honorary member of our band, but that would mean havin' to split the prrrofits. No hard feelings, 'kay?"
  5: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002B [0x21] END_EVENT
  7: 0x002C [0x00] END_REQSTACK()
```

### Event 375

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         1E F0 FF               ...
0030: FF 7F 6F 70 1D 00 80 23  21 00                    ..op...#!.      
```

#### Opcodes

```
  0: 0x002D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0033 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0034 [0x1D] PRINT_EVENT_MESSAGE(message_id=7997*)
    → "Well, well. What's an upstandin' [gent/lady] like yerself doin' in a place like this? You'd best be on yer way, else the Abyssean hordes'll be the least of your worries. Ya catch my drrrift?"
  4: 0x0037 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0038 [0x21] END_EVENT
  6: 0x0039 [0x00] END_REQSTACK()
```

### Event 367

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                00                           .     
```

#### Opcodes

```
  0: 0x003A [0x00] END_REQSTACK()
```

### Event 369

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   00                         .    
```

#### Opcodes

```
  0: 0x003B [0x00] END_REQSTACK()
```

### Event 371

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      00                       .   
```

#### Opcodes

```
  0: 0x003C [0x00] END_REQSTACK()
```
