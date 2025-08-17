# 17772560 - Neraf-Najiruf

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 1060 bytes                |
| Total Events     | 11                        |
| References Count | 27                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [24](#event-24)       | 0x0001       |      1 |              1 |
| [30](#event-30)       | 0x0002       |    111 |             13 |
| [31](#event-31)       | 0x0071       |    106 |             14 |
| [32](#event-32)       | 0x00DB       |    106 |             14 |
| [156](#event-156)     | 0x0145       |     60 |             10 |
| [98](#event-98)       | 0x0181       |    319 |             52 |
| [99](#event-99)       | 0x02C0       |     68 |             12 |
| [97](#event-97)       | 0x0304       |     97 |             15 |
| [10048](#event-10048) | 0x0365       |      7 |              2 |
| [10051](#event-10051) | 0x036C       |     13 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0031      |          49 |
|       1 | 0x2B35      |       11061 |
|       2 | 0x0027      |          39 |
|       3 | 0x2B36      |       11062 |
|       4 | 0x2B4B      |       11083 |
|       5 | 0x2B4C      |       11084 |
|       6 | 0x2B4D      |       11085 |
|       7 | 0x2B57      |       11095 |
|       8 | 0x2B58      |       11096 |
|       9 | 0x2B59      |       11097 |
|      10 | 0x27F1      |       10225 |
|      11 | 0x27F3      |       10227 |
|      12 | 0x27F4      |       10228 |
|      13 | 0x27F5      |       10229 |
|      14 | 0x27F6      |       10230 |
|      15 | 0x27F7      |       10231 |
|      16 | 0x27F8      |       10232 |
|      17 | 0x27F9      |       10233 |
|      18 | 0x0000      |           0 |
|      19 | 0x27FA      |       10234 |
|      20 | 0x27FB      |       10235 |
|      21 | 0x27FC      |       10236 |
|      22 | 0x0001      |           1 |
|      23 | 0x27FE      |       10238 |
|      24 | 0x27FD      |       10237 |
|      25 | 0x2800      |       10240 |
|      26 | 0x2801      |       10241 |

## String References

- **10233**: Do you want to borrow the lantern? [Yes, please./Not now.]

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

### Event 24

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

### Event 30

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 111 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       79 00 11 30 0F 01  10 30 0F 01 79 00 10 30    y..0...0..y..0
0010: 0F 01 11 30 0F 01 66 00  80 F8 FF FF 7F F8 FF FF  ...0..f.........
0020: 7F 74 6C 6B 30 2B 10 30  0F 01 01 80 23 66 00 80  .tlk0+.0....#f..
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 66 02 80 11  ........tlk1f...
0040: 30 0F 01 11 30 0F 01 74  68 6B 31 2B 11 30 0F 01  0...0..thk1+.0..
0050: 03 80 23 66 02 80 11 30  0F 01 11 30 0F 01 74 68  ..#f...0...0..th
0060: 6B 32 53 11 30 0F 01 11  30 0F 01 74 68 6B 32 21  k2S.0...0..thk2!
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x79] Adolie (ID: 17772561/0x010F3011) looks at Neraf-Najiruf (ID: 17772560/0x010F3010) (Basic look)
  1: 0x000C [0x79] Neraf-Najiruf (ID: 17772560/0x010F3010) looks at Adolie (ID: 17772561/0x010F3011) (Basic look)
  2: 0x0016 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  3: 0x0025 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [11061*]:
    → "Did you hear? Some of the Telepoint crystals in Holla, Mea, and Dem have broken into a million pieces!"
  4: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x002D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  6: 0x003C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
  7: 0x004B [0x2B] Adolie (ID: 17772561/0x010F3011) [11062*]:
    → "So that's why Captain Wolfgang has been on edge lately... But what is really going on at those crags?"
  8: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0053 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
 10: 0x0062 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)]
 11: 0x006F [0x21] END_EVENT
 12: 0x0070 [0x00] END_REQSTACK()
```

### Event 31

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0071    |
| Data Size    | 106 bytes |
| Instructions | 14        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    79 00 11 30 0F 01 10  30 0F 01 79 00 10 30 0F   y..0...0..y..0.
0080: 01 11 30 0F 01 66 00 80  F8 FF FF 7F F8 FF FF 7F  ..0..f..........
0090: 74 68 6B 31 2B 10 30 0F  01 04 80 23 66 02 80 11  thk1+.0....#f...
00A0: 30 0F 01 11 30 0F 01 74  6C 6B 30 2B 11 30 0F 01  0...0..tlk0+.0..
00B0: 05 80 23 66 02 80 11 30  0F 01 11 30 0F 01 74 6C  ..#f...0...0..tl
00C0: 6B 31 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 68 6B  k1f..........thk
00D0: 32 2B 10 30 0F 01 06 80  23 21 00                 2+.0....#!.     
```

#### Opcodes

```
  0: 0x0071 [0x79] Adolie (ID: 17772561/0x010F3011) looks at Neraf-Najiruf (ID: 17772560/0x010F3010) (Basic look)
  1: 0x007B [0x79] Neraf-Najiruf (ID: 17772560/0x010F3010) looks at Adolie (ID: 17772561/0x010F3011) (Basic look)
  2: 0x0085 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=49*
  3: 0x0094 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [11083*]:
    → "Did you hear that a super-secret weapon was being loaded onto one of the warships? I wonder what it could be..."
  4: 0x009B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x009C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
  6: 0x00AB [0x2B] Adolie (ID: 17772561/0x010F3011) [11084*]:
    → "Yes, I overheard some of the other guards mention that the society's scientists had built a terrifying new battle machine."
  7: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00B3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
  9: 0x00C2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=49*
 10: 0x00D1 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [11085*]:
    → "Alright! After using that contraption, along with the airships' ultra-powerful mammoth cannons, there won't be enough left of those wyrms to even make dragon burgers!"
 11: 0x00D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x00D9 [0x21] END_EVENT
 13: 0x00DA [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00DB    |
| Data Size    | 106 bytes |
| Instructions | 14        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   79 00 11 30 0F             y..0.
00E0: 01 10 30 0F 01 79 00 10  30 0F 01 11 30 0F 01 66  ..0..y..0...0..f
00F0: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 31 2B 10  ..........thk1+.
0100: 30 0F 01 07 80 23 66 02  80 11 30 0F 01 11 30 0F  0....#f...0...0.
0110: 01 74 6C 6B 30 2B 11 30  0F 01 08 80 23 66 02 80  .tlk0+.0....#f..
0120: 11 30 0F 01 11 30 0F 01  74 6C 6B 31 66 00 80 F8  .0...0..tlk1f...
0130: FF FF 7F F8 FF FF 7F 74  68 6B 32 2B 10 30 0F 01  .......thk2+.0..
0140: 09 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x00DB [0x79] Adolie (ID: 17772561/0x010F3011) looks at Neraf-Najiruf (ID: 17772560/0x010F3010) (Basic look)
  1: 0x00E5 [0x79] Neraf-Najiruf (ID: 17772560/0x010F3010) looks at Adolie (ID: 17772561/0x010F3011) (Basic look)
  2: 0x00EF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=49*
  3: 0x00FE [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [11095*]:
    → "Did you find out anything more about the super-secret weapon the armada took with them?"
  4: 0x0105 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0106 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
  6: 0x0115 [0x2B] Adolie (ID: 17772561/0x010F3011) [11096*]:
    → "No... However, I did hear that the device dealt a severe blow to the mighty Wyrmking during the assault."
  7: 0x011C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x011D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
  9: 0x012C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=49*
 10: 0x013B [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [11097*]:
    → "Wowzie! If I had an ultra-spiffy contraption like that, I'd be eating roast dragon burgers every night!"
 11: 0x0142 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0143 [0x21] END_EVENT
 13: 0x0144 [0x00] END_REQSTACK()
```

### Event 156

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0145   |
| Data Size    | 60 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                1E F0 FF  FF 7F 6F 70 66 00 80 F8       .....opf...
0150: FF FF 7F F8 FF FF 7F 74  6C 6B 30 2B 10 30 0F 01  .......tlk0+.0..
0160: 0A 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0170: 6B 31 53 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 21  k1S........tlk1!
0180: 00                                                .               
```

#### Opcodes

```
  0: 0x0145 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x014A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x014B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x014C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  4: 0x015B [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10225*]:
    → "Sometimes I see the darndest things here. One time, a rookie of ours got cursed in the necropolis of Eldieme, and I didn't know what to do."
  5: 0x0162 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0163 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  7: 0x0172 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  8: 0x017F [0x21] END_EVENT
  9: 0x0180 [0x00] END_REQSTACK()
```

### Event 98

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0181    |
| Data Size    | 319 bytes |
| Instructions | 52        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:    20 01 42 1E F0 FF FF  7F 4A 11 30 0F 01 F0 FF    .B.....J.0....
0190: FF 7F 6F 70 6F 76 11 30  0F 01 66 00 80 F8 FF FF  ..opov.0..f.....
01A0: 7F F8 FF FF 7F 74 6C 6B  30 2B 10 30 0F 01 0B 80  .....tlk0+.0....
01B0: 23 2B 10 30 0F 01 0C 80  23 2B 10 30 0F 01 0D 80  #+.0....#+.0....
01C0: 23 5E 69 64 6C 30 66 02  80 11 30 0F 01 11 30 0F  #^idl0f...0...0.
01D0: 01 74 6C 6B 30 2B 11 30  0F 01 0E 80 23 6B 69 64  .tlk0+.0....#kid
01E0: 6C 30 11 30 0F 01 66 00  80 F8 FF FF 7F F8 FF FF  l0.0..f.........
01F0: 7F 74 6C 6B 30 2B 10 30  0F 01 0F 80 23 2B 10 30  .tlk0+.0....#+.0
0200: 0F 01 10 80 23 5E 69 64  6C 30 24 11 80 12 80 12  ....#^idl0$.....
0210: 80 25 02 00 10 12 80 00  7B 02 66 00 80 F8 FF FF  .%......{.f.....
0220: 7F F8 FF FF 7F 74 6C 6B  30 2B 10 30 0F 01 13 80  .....tlk0+.0....
0230: 23 5E 69 64 6C 30 66 02  80 11 30 0F 01 11 30 0F  #^idl0f...0...0.
0240: 01 74 68 6B 31 2B 11 30  0F 01 14 80 23 66 02 80  .thk1+.0....#f..
0250: 11 30 0F 01 11 30 0F 01  74 68 6B 32 66 00 80 F8  .0...0..thk2f...
0260: FF FF 7F F8 FF FF 7F 74  6C 6B 30 2B 10 30 0F 01  .......tlk0+.0..
0270: 15 80 23 03 01 10 12 80  01 A2 02 02 00 10 16 80  ..#.............
0280: 00 A2 02 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ...f..........tl
0290: 6B 30 2B 10 30 0F 01 17  80 23 03 01 10 16 80 01  k0+.0....#......
02A0: A2 02 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  ..f..........tlk
02B0: 31 53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 21 00  1S........tlk1!.
```

#### Opcodes

```
  0: 0x0181 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0183 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0184 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0189 [0x4A] Adolie (ID: 17772561/0x010F3011) looks at LocalPlayer
  4: 0x0192 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0193 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0194 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0195 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Adolie (ID: 17772561/0x010F3011) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x019A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  9: 0x01A9 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10227*]:
    → "Once I took a new guy to the Eldieme Necropolis, and he got cursed there. He went berserk, and had this unstoppable craving for raw meat."
 10: 0x01B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x01B1 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10228*]:
    → "Well, I gave it some thought... And you know those torches in the rooms made of stone? Well, I heard that spirits hate them..."
 12: 0x01B8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x01B9 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10229*]:
    → "So, I figured it might help if I lit a lantern with those flames and brought it here. That's how we saved the guy."
 14: 0x01C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x01C1 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 16: 0x01C6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
 17: 0x01D5 [0x2B] Adolie (ID: 17772561/0x010F3011) [10230*]:
    → "But, uh... I've also heard that some spirits actually like that kind of fire. So, it might not always be such a good idea."
 18: 0x01DC [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x01DD [0x6B] STOP_AND_IDLE: Adolie (ID: 17772561/0x010F3011) stops current action and resets to idle (animation="idl0")
 20: 0x01E6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
 21: 0x01F5 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10231*]:
    → "I guess we were lucky then. We had no idea what else to do, and just wanted to do what we could."
 22: 0x01FC [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x01FD [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10232*]:
    → "If you want, we can lend you the lantern we used back then. What do you say?"
 24: 0x0204 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0205 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 26: 0x020A [0x24] CREATE_DIALOG(message_id=10233*, default_option=0*, option_flags=0*)
    → "Do you want to borrow the lantern? [Yes, please./Not now.]"
 27: 0x0211 [0x25] WAIT_DIALOG_SELECT()
 28: 0x0212 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x027B
 29: 0x021A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
 30: 0x0229 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10234*]:
    → "Try and bring back the flames in this lantern. We don't know what else could help."
 31: 0x0230 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0231 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 33: 0x0236 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
 34: 0x0245 [0x2B] Adolie (ID: 17772561/0x010F3011) [10235*]:
    → "I seem to remember there were four torches, and that you had to light them in the proper order."
 35: 0x024C [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x024D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
 37: 0x025C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
 38: 0x026B [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10236*]:
    → "Yeah, that's right. I remember screwing that up. Too bad I forgot the real order, though. Well, I'm sure you can figure it out."
 39: 0x0272 [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x0273 [0x03] Work_Zone[1] = 0*
 41: 0x0278 [0x01] GOTO 0x02A2
 42: 0x027B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02A2
 43: 0x0283 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
 44: 0x0292 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10238*]:
    → "Oh, yeah? Well, you're free to use it any time."
 45: 0x0299 [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x029A [0x03] Work_Zone[1] = 1*
 47: 0x029F [0x01] GOTO 0x02A2

SUBROUTINE_02A2:
 48: 0x02A2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
 49: 0x02B1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 50: 0x02BE [0x21] END_EVENT
 51: 0x02BF [0x00] END_REQSTACK()
```

### Event 99

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02C0   |
| Data Size    | 68 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0: 1E F0 FF FF 7F 6F 70 66  00 80 F8 FF FF 7F F8 FF  .....opf........
02D0: FF 7F 74 6C 6B 30 2B 10  30 0F 01 13 80 23 2B 10  ..tlk0+.0....#+.
02E0: 30 0F 01 18 80 23 66 00  80 F8 FF FF 7F F8 FF FF  0....#f.........
02F0: 7F 74 6C 6B 31 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  .tlk1S........tl
0300: 6B 31 21 00                                       k1!.            
```

#### Opcodes

```
  0: 0x02C0 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x02C5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x02C6 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x02C7 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  4: 0x02D6 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10234*]:
    → "Try and bring back the flames in this lantern. We don't know what else could help."
  5: 0x02DD [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x02DE [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10237*]:
    → "Don't forget it's the stone-wrought room that you're after. The torches in the caverns are for something else, so don't mix them up."
  7: 0x02E5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x02E6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  9: 0x02F5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 10: 0x0302 [0x21] END_EVENT
 11: 0x0303 [0x00] END_REQSTACK()
```

### Event 97

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0304   |
| Data Size    | 97 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0300:             1E F0 FF FF  7F 4A 11 30 0F 01 F0 FF      .....J.0....
0310: FF 7F 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0320: 6C 6B 30 2B 10 30 0F 01  19 80 23 5E 69 64 6C 30  lk0+.0....#^idl0
0330: 66 02 80 11 30 0F 01 11  30 0F 01 74 6C 6B 30 2B  f...0...0..tlk0+
0340: 11 30 0F 01 1A 80 23 66  02 80 11 30 0F 01 11 30  .0....#f...0...0
0350: 0F 01 74 6C 6B 31 53 11  30 0F 01 11 30 0F 01 74  ..tlk1S.0...0..t
0360: 6C 6B 31 21 00                                    lk1!.           
```

#### Opcodes

```
  0: 0x0304 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0309 [0x4A] Adolie (ID: 17772561/0x010F3011) looks at LocalPlayer
  2: 0x0312 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0313 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0314 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  5: 0x0323 [0x2B] Neraf-Najiruf (ID: 17772560/0x010F3010) [10240*]:
    → "Oh, the flame thing didn't work, huh? Well, I'm just glad the spirit's gone!"
  6: 0x032A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x032B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  8: 0x0330 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
  9: 0x033F [0x2B] Adolie (ID: 17772561/0x010F3011) [10241*]:
    → "Yep, I knew it. You learn something every day. I'm gonna write this up in the Guardsman's Daily."
 10: 0x0346 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0347 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)], work=39*
 12: 0x0356 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [Adolie (ID: 17772561/0x010F3011), Adolie (ID: 17772561/0x010F3011)]
 13: 0x0363 [0x21] END_EVENT
 14: 0x0364 [0x00] END_REQSTACK()
```

### Event 10048

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0365  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0360:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x0365 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x036B [0x00] END_REQSTACK()
```

### Event 10051

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x036C   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0360:                                      92 01 F8 FF              ....
0370: FF 7F 94 01 F8 FF FF 7F  00                       .........       
```

#### Opcodes

```
  0: 0x036C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0372 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0378 [0x00] END_REQSTACK()
```
